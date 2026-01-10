# This script is responsible for generating bundles of models
# with specific properties. You can select:
# - model format
# - how inputs are treated (constant/identity/free)
# - filter condition expression


from pathlib import Path
from os import listdir, mkdir
from os.path import isdir, isfile
from biodivine_aeon import *
from datetime import datetime
from utils import inputs_free, inputs_constant, inputs_identity, output_model

import json
import random
import argparse

format_choices = ["bnet", "aeon", "sbml", "bma", "booleannet"]
input_choices = ["true", "false", "identity", "free", "random"]
graph_choices = ["original", "inferred"]
filter_help_text = """Enter filter expression satisfied by the desired models [default: no filter].
The filter expression is a Python expression that evaluates to True/False.
You can assume `variables` and `inputs` are lists of entity names (strings).
Variable `regulations` is a list of pairs of entity names.
Variable `metadata` is a dictionary representing the `metadata.json` file.
Finally, variable `model` is an AEON.py Boolean network.
"""

parser = argparse.ArgumentParser(
	description="This script is responsible for generating bundles of models with specific properties.",
)
parser.add_argument("-f", "--format", choices=format_choices)
parser.add_argument("-i", "--inputs", choices=input_choices)
parser.add_argument("-g", "--graph", choices=graph_choices)
parser.add_argument("--filter", help=filter_help_text)
parser.add_argument("-o", "--output-dir")
args = parser.parse_args()

ENDC = '\033[0m'
BOLD = '\033[1m'

# Read desired model format from user input.

FORMAT = "aeon"
while True:
	if args.format is not None:
		user_format = args.format
	else:
		print("Choose model format [aeon/bnet/sbml/bma/booleannet; default: aeon]")
		print(BOLD, end="")
		user_format = input().lower()
		print(ENDC, end="")

	if user_format == "":
		user_format = "aeon"
	if user_format in format_choices:
		FORMAT = user_format
		print(f"Selected output format: {BOLD}{user_format}{ENDC}")
		break
	print("Invalid format chosen.")

# Read desired input representation from user input.

INPUTS = "free"
while True:
	if args.inputs is not None:
		user_inputs = args.inputs
	else:
		print("Choose the representation of model inputs (i.e. source nodes) [true/false/identity/free/random; default: free]")
		print(BOLD, end="")	
		user_inputs = input().lower()
		print(ENDC, end="")

	if user_inputs == "":
		user_inputs = "free"

	if user_inputs == "free" and (FORMAT == "bma" or FORMAT == "booleannet"):
		print("The BMA and Booleannet formats do not support free parameters.")
		continue

	if user_inputs in input_choices:
		INPUTS = user_inputs
		print(f"Selected input representation: {BOLD}{user_inputs}{ENDC}")
		break
	print("Invalid representation chosen.")

GRAPH = "original"
while True: 
	if args.inputs is not None:
		user_graph = args.graph
	else:
		print("Do you want to use the original, or inferred regulatory graph [original/inferred; default: original]")
		print(BOLD, end="")	
		user_graph = input().lower()
		print(ENDC, end="")

	if user_graph == "":
		user_graph = "original"

	if user_graph in graph_choices:
		GRAPH = user_graph
		print(f"Selected graph representation: {BOLD}{user_inputs}{ENDC}")
		break
	print("Invalid representation chosen.")

SAMPLE_COUNT = 0
SAMPLE_SEED = 0
if INPUTS == "random":
	while True:
		print("Choose how many unique random input valuations should be sampled (at most) [positive integer; default: 32]")
		print(BOLD, end="")
		try:
			user_count = input().lower()
			print(ENDC, end="")
			if user_count == "":
				user_count_int = 32
			else:
				user_count_int = int(user_count)
			if user_count_int > 0:
				SAMPLE_COUNT = user_count_int
				print(f"Selected {BOLD}{user_count}{ENDC} random samples.")
				break
		except:
			print(ENDC, end="")
			print("Invalid sample count.")	
	while True:
		print("Choose a seed for random sampling [integer; default: 0]")
		print(BOLD, end="")
		try:
			user_seed = input().lower()
			print(ENDC, end="")
			if user_seed == "":
				user_seed_int = 0
			else:
				user_seed_int = int(user_seed)
			SAMPLE_SEED = user_seed_int
			print(f"Selected {BOLD}{user_seed}{ENDC} as the random seed.")
			break
		except:
			print(ENDC, end="")
			print("Invalid seed.")	

# Read filter string from user input.

model_directories = list(listdir("models"))
model_directories.sort()
model_directories = list(filter(lambda d: isdir("models/"+d), model_directories))

def check_filter(filter, model_dir):
	model = BooleanNetwork.from_aeon(Path(f"models/{model_dir}/model.aeon").read_text())	
	variables = []
	inputs = []
	regulations = []
	for var in model.variables():
		name = model.get_variable_name(var)
		if len(model.predecessors(var)) == 0:
			inputs.append(name)
		else:
			variables.append(name)
		for reg in model.predecessors(var):
			reg_name  = model.get_variable_name(reg)
			regulations.append((reg_name, name))
	
	metadata = {}
	with open(f"models/{model_dir}/metadata.json") as file:
		metadata = json.load(file)

	return eval(filter, {}, {
		'variables': variables,
		'inputs': inputs,
		'regulations': regulations,
		'model': model,
		'metadata': metadata,
	})


FILTER = "True"
while True:
	if args.filter is not None:
		user_filter = args.filter
	else:
		print("Enter filter expression satisfied by the desired models [default: no filter].")
		print(" > The filter expression is a Python expression that evaluates to True/False.")
		print(" > You can assume `variables` and `inputs` are lists of entity names (strings).")
		print(" > Variable `regulations` is a list of pairs of entity names.")
		print(" > Variable `metadata` is a dictionary representing the `metadata.json` file.")
		print(" > Finally, variable `model` is an AEON.py Boolean network.")
		print(BOLD, end="")
		user_filter = input().lower()
		print(ENDC, end="")
	if user_filter == "":		
		print("No filter given. All models will be included.")
		break
	else:
		print("Computing the number of models after filtering...")
		total = 0
		for model_dir in model_directories:
			if check_filter(user_filter, model_dir):
				total += 1

		print(f"Models satisfying this filter: {BOLD}{total}{ENDC}")
		print("Keep this filter? [yes/no; default: yes]")
		print(BOLD, end="")
		change = input().lower()
		print(ENDC, end="")
		if change == "no":
			continue
		else:
			FILTER = user_filter
			print(f"Filter selected: {BOLD}{FILTER}{ENDC}")
			break

OUT_DIR = "bbm-edition"

while True:
	if args.output_dir is not None:
		user_dir = args.output_dir
	else:
		print("Choose output directory: [default: bbm-edition]")
		print(BOLD, end="")
		user_dir = input().lower()
		print(ENDC, end="")

	if user_dir != "":
		OUT_DIR = user_dir
	if isfile(OUT_DIR) or isdir(OUT_DIR):
		print(f"A file/directory with this name already exists. Choose a different one.")
	else:
		print(f"Selected output directory: {BOLD}{OUT_DIR}{ENDC}")
		break


print(f" ... Writing BBM edition models to {OUT_DIR} ... ")

mkdir(OUT_DIR)

meta_csv_summary = "ID, name, variables, regulations\n"

for model_dir in model_directories:
	if check_filter(FILTER, model_dir):
		print(f" > Outputting {model_dir}")
		model = BooleanNetwork.from_aeon(Path(f"models/{model_dir}/model.aeon").read_text())

		metadata = {}
		with open(f"models/{model_dir}/metadata.json") as file:
			metadata = json.load(file)

		meta_csv_summary += f"{metadata['id']:03d}, {metadata['name']}, {metadata['variables']}, {metadata['inputs']}, {metadata['regulations']}\n"

		if INPUTS == "random":
			# For random sampling, we have to be a bit more clever...
			param_model = inputs_free(model)
			stg = AsynchronousGraph(param_model)
			const_model = inputs_constant(model, True)			
			all_colors = stg.mk_unit_colors()			
			if all_colors.is_singleton():
				# This model does not have inputs, we can just output it.				
				output_model(OUT_DIR, const_model, metadata['id'], FORMAT, infer_graph=(GRAPH == "inferred"))
			else:
				ctx = stg.symbolic_context()
				bdd_vars = ctx.bdd_variable_set()
				rng = random.Random(SAMPLE_SEED)

				# Prepare a mapping from variable names to their corresponding symbolic 
				# parameter variables.				
				input_symbolic_var = {}
				for var in param_model.implicit_parameters():
					name = param_model.get_variable_name(var)
					table = ctx.get_function_table(var)
					assert len(table) == 1
					symbolic_var = table[0][1]
					input_symbolic_var[name] = symbolic_var

				print(f" >> Sampling... ", end="")
				for s in range(SAMPLE_COUNT):					
					if all_colors.is_empty():
						# This model has fewer valuations than the sample count.
						break
					print(f"{s+1}; ", end="")

					# Here, we pick a random valuation and subtract it from the set of colors.
					# Unfortunately, there doesn't seem to be a nicer way to do this atm.
					# But it would be cool to add this to the API in the future.

					valuation_seed = rng.randrange(0, 2**30)
					valuation_sample = all_colors.to_bdd().valuation_random(valuation_seed)
					valuation_bdd = bdd_vars.mk_conjunctive_clause(valuation_sample)
					# We have to project away the state variables from the valuation
					# and this seems to be the easiest way to do it.
					valuation_set = ColoredVertexSet(ctx, valuation_bdd)
					all_colors = all_colors.minus(valuation_set.colors())

					suffix = "_"
					for (name, bdd_var) in input_symbolic_var.items():
						if valuation_sample[bdd_var]:
							suffix += "1"
							const_model.set_update_function(name, UpdateFunction.mk_const(const_model, True))
						else:
							suffix += "0"
							const_model.set_update_function(name, UpdateFunction.mk_const(const_model, False))
					output_model(OUT_DIR, const_model, metadata['id'], FORMAT, suffix, infer_graph=(GRAPH == "inferred"))
				print(" Done.")
		else:
			if INPUTS == "free":
				model = inputs_free(model)
			if INPUTS == "true":
				model = inputs_constant(model, True)
			if INPUTS == "false":
				model = inputs_constant(model, False)
			if INPUTS == "identity":
				model = inputs_identity(model)

			output_model(OUT_DIR, model, metadata['id'], FORMAT, infer_graph=(GRAPH == "inferred"))


Path(f'{OUT_DIR}/summary.csv').write_text(meta_csv_summary)
print(f"Dataset summary written to `{OUT_DIR}/summary.csv`.")

with open(f'{OUT_DIR}/metadata.json', "w") as file:
	metadata = {
		'timestamp': f"{datetime.now()}",
		'model_format': FORMAT,
		'input_representation': INPUTS,
		'filter_expression': FILTER,
		'output_dir': OUT_DIR,
	}
	if INPUTS == "random":
		metadata['sample_count'] = SAMPLE_COUNT
		metadata['sample_seed'] = SAMPLE_SEED
	json.dump(metadata, file)
print(f"Dataset metadata written to `{OUT_DIR}/metadata.json`.")
