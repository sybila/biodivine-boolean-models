from biodivine_aeon import BooleanNetwork

# Common types of errors:
#  - Variable is unused
#  - Variable is an input
#  - Regulation monotonicity mismatch
#  - Regulation essentiality mismatch
#  - Other
#  - Dangerous variable name (does not match [a-z][A-Z0-9_]*)

# https://biodivine.fi.muni.cz/docs/aeon-py/latest/biodivine_aeon.html

def report_errors_sbml(file_content) -> [str]:
	parsing_errors = []
	... parse ...
	if len(parsing_errors) == 0:
		report_errors(bn)
	return 
		parsing_errors


def report_errors_bnet(file_content) -> [str]:
	parsing_errors = []
	... parse ...
	if len(parsing_errors) == 0:
		report_errors(bn)
	return 
		parsing_errors

def report_errors_aeon(file_content) -> [str]:
	parsing_errors = []
	... parse ...
	if len(parsing_errors) == 0:
		report_errors(bn)
	return 
		parsing_errors



def report_errors(bn: BooleanNetwork) -> [str]:
	pass