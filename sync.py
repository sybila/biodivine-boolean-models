import re
import sys
import json

from pathlib import Path
from os import listdir, mkdir
from os.path import isfile, isdir, join
from biodivine_aeon import *

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

def check_metadata(id, name, metadata):
	if metadata['id'] != id:
		print("ERROR: Invalid id in metadata of", name)
		sys.exit(128)

	if metadata['name'] != name:
		print("ERROR: Invalid name in metadata of", name)
		sys.exit(128)

	if metadata['url-publication'] == None:
		print("ERROR: Missing publication url in", name)
		sys.exit(128)

	if metadata['url-model'] == None:
		print("ERROR: Missing model url in", name)
		sys.exit(128)

def check_unused_variables(model):
	graph = model.graph()
	for var in graph.variables():
		name = graph.get_variable_name(var)
		if len(graph.regulators(var)) == 0 and len(graph.targets(var)) == 0:			
			print("ERROR: Variable", name, "is unused.")
			sys.exit(128)
		if model.get_update_function(var) == name and len(graph.regulators(var)) <= 1:
			print("ERROR: Variable", name, "is effectively an input.")
			sys.exit(128)

def erase_inputs(model):
	graph = model.graph()
	for var in graph.variables():
		if len(graph.regulators(var)) == 0:
			model.set_update_function(var, None)
	return model

def check_integrity(model):
	# This will throw an error if the model is invalid.
	async_graph = SymbolicAsyncGraph(model)

def model_stats(model):
	graph = model.graph()
	variables = 0
	inputs = 0
	for var in graph.variables():
		if len(graph.regulators(var)) == 0:
			inputs += 1
		else:
			variables += 1
	return (variables, inputs, len(graph.regulations()))

def fix_variable_names(model):
	# Ensures that every variable starts with v_,
	# otherwise bnet may have problems with invalid names.
	graph = model.graph()
	for var in graph.variables():
		name = graph.get_variable_name(var)
		model.set_variable_name(var, "v_"+name)				
	return model

source_directories = list(listdir("sources"))
source_directories.sort()

for model_dir in source_directories:
	if model_dir.startswith("."):
		# Skip hidden files.
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

	check_metadata(model_id, model_name, metadata)


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
	
	if model == None:
		print("ERROR: Missing source.sbml/.bnet/.aeon in", source_file)
		sys.exit(128)

	# Static analysis (unused variables/regulations, etc.)
	check_unused_variables(model)
	model = erase_inputs(model)
	check_integrity(model)
	model = fix_variable_names(model)
	print("\t - Model is OK.")

	(variables, inputs, regulations) = model_stats(model)
	print(	"\t - Model has", 
			variables, "variables,", 
			inputs, "inputs, and", 
			regulations, "regulations.")

	metadata['variables'] = variables
	metadata['inputs'] = inputs
	metadata['regulations'] = regulations

	output_directory = f'[id-{model_id:03d}]__[var-{variables}]__[in-{inputs}]__[{model_name}]'
	
	if not isdir('models/'+output_directory):
		mkdir('models/'+output_directory)

	# Write model outputs
	Path(f'models/{output_directory}/model.aeon').write_text(model.to_aeon())
	Path(f'models/{output_directory}/model.sbml').write_text(model.to_sbml())
	Path(f'models/{output_directory}/model.bnet').write_text(model.to_bnet())

	with open(f'models/{output_directory}/metadata.json', "w") as file:
		json.dump(metadata, file)

	readme = f'# \\[{model_id:03d}\\] {model_name}\n\n'
	readme += f' - Variables: {variables}\n'
	readme += f' - Inputs: {inputs}\n'
	readme += f' - Regulations: {regulations}\n'
	readme += f' - Publication: {metadata["url-publication"]}\n'
	readme += f' - Source: {metadata["url-model"]}\n'
	readme += "\n\n"

	readme += notes

	readme += "\n\n### Model citation"
	readme += "\n\n```\n"
	readme += bib
	readme += "\n```\n\n"
	Path(f'models/{output_directory}/README.md').write_text(readme)

	print("\t - Model exported into", output_directory)