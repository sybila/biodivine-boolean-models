from biodivine_aeon import *
from pathlib import Path
from os.path import exists
import csv
import sys

model_variables = set()
model_regulations = set()
model_functions = {}

# First, read the links file and construct a regulatory
# network based on this data.

# Note that dashes in variable names are not supported.
# While reading the file, we thus have to also replace
# them with underscores.

def fix_name(name):
	return name.replace("-", "_")

with open('source.links.tsv', newline='') as links_file:
	links = csv.reader(links_file, delimiter='\t')	
	for link in links:
		source = fix_name(link[0])
		op = link[1]
		target = fix_name(link[2])
		model_variables.add(source)
		model_variables.add(target)
		
		if op == '+':
			model_regulations.add(f"{source} -> {target}")
		elif op == '-':
			model_regulations.add(f"{source} -| {target}")
		elif op == '+/-':
			model_regulations.add(f"{source} -? {target}")
		else:
			print("Unknown regulation:", op)
			sys.exit(128)

rg = RegulatoryGraph(list(model_variables))

for reg in model_regulations:
	rg.add_regulation(reg)

#print(f"Loaded a regulatory network with {len(model_variables)} variables and {len(rg.regulations())} regulations.")

# Helper function for creating DNF literals.
def mk_literal(x):
	(name, value) = x
	if value == '1':
		return name
	elif value == '0':
		return "!"+name
	else: 
		print("Unknown value", value)
		sys.exit(128)

bn = BooleanNetwork(rg)

for var in rg.variables():
	name = rg.get_variable_name(var)
	# Only translate functions for non-inputs
	if len(rg.regulators(var)) > 0:		
		# Here, we translate the logical truth table to a DNF
		# representation. This is not very efficient, but
		# should be sufficient for our use case.
		formula = []
		with open(f'source.truth_tables/{name}.txt', newline='') as table_file:
			table = list(csv.reader(table_file, delimiter='\t'))
			header = list(map(fix_name, table[0]))
			for row in table[1:]:
				# DNF only contains positive rows.
				if row[-1] == '1':
					# The clause skips the last value because it is the output.
					clause = list(zip(header[:-1], row[:-1]))					
					clause = " & ".join(list(map(mk_literal, clause)))
					formula.append("("+clause+")")
		formula = " | ".join(formula)		
		bn.set_update_function(name, formula)

print(bn.to_aeon())