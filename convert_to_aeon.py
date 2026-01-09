from biodivine_aeon import *
import sys
import re

bn = BooleanNetwork.from_file(sys.argv[1])

# Normalize variable names that don't match [a-zA-Z0-9_]+
pattern = re.compile(r'^[a-zA-Z0-9_]+$')
for var in bn.variables():
    name = bn.get_variable_name(var)
    if not pattern.match(name):
        # Replace any character that's not alphanumeric or underscore with underscore
        normalized = re.sub(r'[^a-zA-Z0-9_]', '_', name)
        # Collapse multiple consecutive underscores into a single one
        normalized = re.sub(r'_+', '_', normalized)
        # Remove leading/trailing underscores
        normalized = normalized.strip('_')
        # If name becomes empty, use a default name
        if not normalized:
            normalized = 'var'
        bn.set_variable_name(var, normalized)

print(bn.to_aeon())
