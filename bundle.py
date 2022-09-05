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
from utils import inputs_free, inputs_constant, inputs_identity

import json

ENDC = '\033[0m'
BOLD = '\033[1m'

# Read desired model format from user input.

FORMAT = "aeon"
while True:
	print("Choose model format [bnet/aeon/sbml; default: aeon]")
	print(BOLD, end="")
	user_format = input().lower()
	print(ENDC, end="")
	if user_format == "":
		user_format = "aeon"
	if user_format in ["bnet", "aeon", "sbml"]:
		FORMAT = user_format
		print(f"Selected output format: {BOLD}{user_format}{ENDC}")
		break
	print("Invalid format chosen.")

# Read desired input representation from user input.

INPUTS = "free"
while True:
	print("Choose how model inputs are represented [true/false/identity/free; default: free]")
	print(BOLD, end="")	
	user_inputs = input().lower()
	print(ENDC, end="")
	if user_inputs == "":
		user_inputs = "free"
	if user_inputs in ["true", "false", "identity", "free"]:
		INPUTS = user_inputs
		print(f"Selected input representation: {BOLD}{user_inputs}{ENDC}")
		break
	print("Invalid representation chosen.")

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
		if len(model.graph().regulators(var)) == 0:
			inputs.append(name)
		else:
			variables.append(name)
		for reg in model.graph().regulators(var):
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

		if INPUTS == "free":
			model = inputs_free(model)
		if INPUTS == "true" or INPUTS == "false":
			model = inputs_constant(model, INPUTS)
		if INPUTS == "identity":
			model = inputs_identity(model)

		if FORMAT == "aeon":
			Path(f"{OUT_DIR}/{metadata['id']:03d}.aeon").write_text(model.to_aeon())
		if FORMAT == "bnet":
			Path(f"{OUT_DIR}/{metadata['id']:03d}.bnet").write_text(model.to_bnet())
		if FORMAT == "sbml":
			Path(f"{OUT_DIR}/{metadata['id']:03d}.sbml").write_text(model.to_sbml())


Path(f'{OUT_DIR}/summary.csv').write_text(meta_csv_summary)
print(f"Dataset summary written to `{OUT_DIR}/summary.csv`.")

with open(f'{OUT_DIR}/metadata.json', "w") as file:
	json.dump({
		'timestamp': f"{datetime.now()}",
		'model_format': FORMAT,
		'input_representation': INPUTS,
		'filter_expression': FILTER,
		'output_dir': OUT_DIR,
	}, file)
print(f"Dataset metadata written to `{OUT_DIR}/metadata.json`.")
