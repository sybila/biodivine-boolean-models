import os
from biodivine_aeon import *

# This script counts the total number of variables,
# regulators, and variables that are not inputs/constants.

total_regulations = 0
total_variables = 0
total_non_inputs = 0
for file in os.listdir('./sbml-true'):
	if not file.endswith('.sbml'):
		continue
	bn = BooleanNetwork.from_file('./sbml-true/'+file)
	for var in bn.variables():
		total_variables += 1
		regs = bn.predecessors(var)
		total_regulations += len(regs)
		if len(regs) > 0:
			total_non_inputs += 1
print(total_regulations)
print(total_variables)
print(total_non_inputs)