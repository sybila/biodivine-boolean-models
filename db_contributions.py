# This script reads the dataset and compiles 
# the number of contributions from individual sources.

from pathlib import Path
from os import listdir
from os.path import isdir

import json

SOURCES = set(["cell-collective", "ginsim", "biomodels", "covid-disease-map"])

model_directories = list(listdir("models"))
model_directories.sort()
model_directories = list(filter(lambda d: isdir("models/"+d), model_directories))

other = 0
unique_count = { s:0 for s in SOURCES }
shared_count = { s:0 for s in SOURCES }

for model_dir in model_directories:
	metadata = {}
	with open(f"models/{model_dir}/metadata.json") as file:
		metadata = json.load(file)
	keywords = set(metadata['keywords'])
	sources = list(SOURCES & keywords)
	if len(sources) == 0:
		other += 1
	elif len(sources) == 1:
		unique_count[sources[0]] += 1
	else:
		for s in sources:
			shared_count[s] += 1

for s in SOURCES:
	print(f"[{s}] Total models: {unique_count[s] + shared_count[s]}")
	print(f"[{s}] Unique models: {unique_count[s]}")
	print(f"[{s}] Shared models: {shared_count[s]}")	
print(f"Other source: {other}")
