from biodivine_aeon import *
from pathlib import Path
from re import search

regulations = Path("source.regulations.sif").read_text()
regulations = regulations.split("\n")
print(regulations)

variables = set()
for reg in regulations:
	if reg == '':
		print("Skip empty line.")
		continue
	match = search('(.+?)\\s+-[>|]\\s+(.+)', reg)
	variables.add(match.group(1))
	variables.add(match.group(2))
	print(f"Matched variables `{match.group(1)}` and `{match.group(2)}` in regulation `{reg}`.")

rn = RegulatoryGraph(list(variables))

for reg in regulations:
	if reg == '':
		continue
	rn.add_regulation(reg)

print(f"Created regulatory network with {len(rn.regulations())} regulations.")

bn = BooleanNetwork(rn)

for target in bn.variables():
	positive = []
	negative = []
	for source in rn.regulators(target):
		reg = rn.find_regulation(source, target)		
		if reg['monotonicity'] == 'activation':
			positive.append(rn.get_variable_name(source))
		if reg['monotonicity'] == 'inhibition':
			negative.append(rn.get_variable_name(source))
		
	#print("Positive:", positive)
	#print("Negative:", negative)

	function = ""
	if len(positive) == 0 and len(negative) == 0:
		# Inputs remain without functions
		continue
	elif len(negative) == 0:
		# Only positive inputs
		function = " | ".join(positive)
	elif len(positive) == 0:
		# Only negative inputs
		nf = " | ".join(negative)
		function = f"!({nf})"
	else:
		# General function
		pf = " | ".join(positive)
		nf = " | ".join(negative)
		function = f"({pf}) & !({nf})"
	
	print(function)
	bn.set_update_function(target, function)	

Path("source.aeon").write_text(bn.to_aeon())