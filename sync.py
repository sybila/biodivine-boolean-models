# This script is reponsible for reading, validating and translating 
# models in the /sources directory and writing the final results
# into the /models directory. As part of this process, it generates
# basic metadata about the model's structure.

import re
import sys
import json

from pathlib import Path
from os import listdir, mkdir
from os.path import isfile, isdir, join
from biodivine_aeon import *

from utils import input_list, inputs_identity, normalize_names, output_list, variable_list

if not isdir("sources"):
	print("ERROR: Missing input `sources` directory.")
	sys.exit(128)

if not isdir("models"):
	print("ERROR: Missing output `models` directory.")
	sys.exit(128)

def read_dir_name(dir_name):
	result = re.search("(\\d+)_([A-Z0-9-]+)", dir_name)
	if result == None:
		print("ERROR: Invalid source directory:", dir_name)
	return (int(result.group(1)), result.group(2))	

def check_metadata(id, name, metadata, bib):
	if (not 'id' in metadata) or metadata['id'] != id:
		print("ERROR: Invalid id in metadata of", name)
		sys.exit(128)

	if (not 'name' in metadata) or metadata['name'] != name:
		print("ERROR: Invalid name in metadata of", name)
		sys.exit(128)

	if(not 'url-publication' in metadata) or metadata['url-publication'] == None:
		print("ERROR: Missing publication url in", name)
		sys.exit(128)

	if (not 'url-model' in metadata) or metadata['url-model'] == None:
		print("ERROR: Missing model url in", name)
		sys.exit(128)

	if (not 'keywords' in metadata) or (metadata['keywords'] == None):
		print("ERROR: Missing keywords attribute in", name)
		sys.exit(128)

	if (not f'bbm-{int(id):03d}' in bib):
		print(f"ERROR: Missing a `bbm-{int(id):03d}` key in the `citation.bib` file.")
		sys.exit(128)

def check_unused_variables(model: BooleanNetwork):
	errors = 0
	for var in model.variables():
		name = model.get_variable_name(var)
		if len(model.predecessors(var)) == 0 and len(model.successors(var)) == 0:			
			print("ERROR: Variable", name, "is unused.")
			errors += 1
		function = model.get_update_function(var)		
		if function is not None and function.as_var() == var and len(model.predecessors(var)) <= 1:
			print("ERROR: Variable", name, "is effectively an input.")
			errors += 1
	if errors > 0:
		sys.exit(128)

def erase_inputs(model: BooleanNetwork):
	for var in model.variables():
		if len(model.predecessors(var)) == 0:
			model.set_update_function(var, None)
	return model

def check_integrity(model: BooleanNetwork):
	# This will throw an error if the model is invalid.
	async_graph = AsynchronousGraph(model)
	assert async_graph.network_variable_count() == model.variable_count()

def model_stats(model: BooleanNetwork):
	variables = 0
	inputs = 0
	for var in model.variables():
		if len(model.predecessors(var)) == 0:
			inputs += 1
		else:
			variables += 1
	return (variables, inputs, len(model.regulations()))

def fix_variable_names(model: BooleanNetwork):
	# Ensures that every variable starts with v_,
	# otherwise bnet may have problems with invalid names.
	for var in model.variables():
		name = model.get_variable_name(var)
		model.set_variable_name(var, "v_"+name)				
	return model

source_directories = list(listdir("sources"))
source_directories.sort()

if len(sys.argv) > 1:
	test_id = sys.argv[1]
else:
	test_id = None

meta_csv_summary = "ID, name, variables, inputs, regulations\n"

for model_dir in source_directories:
	if model_dir.startswith("."):
		# Skip hidden files.
		continue

	if test_id and not model_dir.startswith(test_id):
		continue

	(model_id, model_name) = read_dir_name(model_dir)

	if model_name == "TEMPLATE":
		# Skip template directories
		continue

	print("Start processing ", model_dir)

	# Check that the model has all metadata prepared.
	metadata_file = "sources/" + model_dir + "/metadata.json"	
	notes_file = "sources/" + model_dir + "/notes.md"
	bib_file = "sources/" + model_dir + "/citation.bib"

	if not isfile(metadata_file):
		print("ERROR: Missing metadata.json in", model_dir)
		sys.exit(128)

	if not isfile(notes_file):
		print("ERROR: Missing notes.md in", model_dir)
		sys.exit(128)

	if not isfile(bib_file):
		print("ERROR: Missing citation.bib in", model_dir)
		sys.exit(128)

	notes = Path(notes_file).read_text()
	bib = Path(bib_file).read_text()
	metadata = {}
	with open(metadata_file) as file:
		metadata = json.load(file)

	check_metadata(model_id, model_name, metadata, bib)


	# Load the model (including syntactic check)
	model = None
	if isfile(f'sources/{model_dir}/source.sbml'):
		source = Path(f'sources/{model_dir}/source.sbml').read_text()
		model = BooleanNetwork.from_sbml(source)
	if isfile(f'sources/{model_dir}/source.aeon'):
		source = Path(f'sources/{model_dir}/source.aeon').read_text()
		model = BooleanNetwork.from_aeon(source)
	if isfile(f'sources/{model_dir}/source.bnet'):
		source = Path(f'sources/{model_dir}/source.bnet').read_text()
		model = BooleanNetwork.from_bnet(source)
	if isfile(f'sources/{model_dir}/source.bma.json'):
		source = Path(f'sources/{model_dir}/source.bma.json').read_text()
		model = BooleanNetwork.from_bma_json(source)
	if isfile(f'sources/{model_dir}/source.booleannet.txt'):
		source = Path(f'sources/{model_dir}/source.booleannet.txt').read_text()
		model = BooleanNetwork.from_booleannet(source)
	
	if model == None:
		print("ERROR: Missing source.sbml/.bnet/.aeon/.bma.json/.booleannet.txt in", model_dir)
		sys.exit(128)

	# Static analysis (unused variables/regulations, etc.)
	check_unused_variables(model)
	model = erase_inputs(model)
	check_integrity(model)
	model = fix_variable_names(model)
	normalize_names(model)
	print("\t - Model is OK.")

	(variables, inputs, regulations) = model_stats(model)
	print(	"\t - Model has", 
			variables, "variables,", 
			inputs, "inputs, and", 
			regulations, "regulations.")

	metadata['variables'] = variables
	metadata['variable-names'] = variable_list(model)
	metadata['inputs'] = inputs
	metadata['input-names'] = input_list(model)
	metadata['output-names'] = output_list(model)
	metadata['regulations'] = regulations
	metadata['notes'] = notes
	metadata['bib'] = bib

	# Add a row to the metadata summary csv:
	meta_csv_summary += f"{model_id:03d}, {model_name}, {variables}, {inputs}, {regulations}\n"
	
	output_directory = f'[id-{model_id:03d}]__[var-{variables}]__[in-{inputs}]__[{model_name}]'
	
	if not isdir('models/'+output_directory):
		mkdir('models/'+output_directory)

	# Write model outputs

	# (for BMA and booleannet, we have to use identity inputs)
	model_identity = inputs_identity(model)

	Path(f'models/{output_directory}/model.aeon').write_text(model.to_aeon())
	Path(f'models/{output_directory}/model.inferred-graph.aeon').write_text(model.infer_valid_graph().to_aeon())
	Path(f'models/{output_directory}/model.sbml').write_text(model.to_sbml())
	Path(f'models/{output_directory}/model.bnet').write_text(model.to_bnet())
	Path(f'models/{output_directory}/model.bma.json').write_text(model_identity.to_bma_json(pretty=True))
	Path(f'models/{output_directory}/model.booleannet.txt').write_text(model_identity.to_booleannet())

	with open(f'models/{output_directory}/metadata.json', "w") as file:
		json.dump(metadata, file, indent=4)

	readme = f'# \\[{model_id:03d}\\] {model_name}\n\n'
	readme += f' - Variables: {variables}\n'
	readme += f' - Inputs: {inputs}\n'
	readme += f' - Regulations: {regulations}\n'
	readme += f' - Publication: {metadata["url-publication"]}\n'
	readme += f' - Source: {metadata["url-model"]}\n'
	readme += f' - Keywords: {", ".join(metadata["keywords"])}\n'
	readme += "\n\n"

	readme += notes

	readme += "\n\n### Model citation"
	readme += "\n\n```\n"
	readme += bib
	readme += "\n```\n\n"
	Path(f'models/{output_directory}/README.md').write_text(readme)

	print("\t - Model exported into", output_directory)

Path(f'models/summary.csv').write_text(meta_csv_summary)
print("Dataset summary written to `models/summary.csv`.")
