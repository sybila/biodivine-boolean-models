#!/usr/bin/env python3
"""
Convert logical rules file to .bnet Boolean network format.

The script:
1. Splits each rule based on '<-'
2. Replaces '+' with '&' (conjunction)
3. Merges multiple rules for the same variable into a disjunction (OR)
4. Outputs the result as a .bnet Boolean network (replacing / and - with _ in variable names)
"""

from pathlib import Path
import sys
from collections import defaultdict

def parse_rules(input_file):
    """Parse the logical rules file and return a dictionary of variable -> expression list."""
    rules = defaultdict(list)
    
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Split on '<-'
            if '<-' not in line:
                continue
            
            parts = line.split('<-', 1)
            if len(parts) != 2:
                continue
            
            target = parts[0].strip().replace('/', '_').replace('-', '_')
            expression = parts[1].strip().replace('/', '_').replace('-', '_')
            
            # Replace '+' with '&' (conjunction)
            expression = expression.replace('+', ' & ')
            
            rules[target].append(expression)
    
    return rules

def merge_rules(rules_dict):
    """Merge multiple rules for the same variable into a disjunction."""
    merged = {}
    
    for variable, expressions in rules_dict.items():
        if len(expressions) == 1:
            merged[variable] = expressions[0]
        else:
            # Combine multiple expressions with OR (|)
            # Wrap each expression in parentheses for clarity
            merged[variable] = ' | '.join(f'({expr})' for expr in expressions)
    
    return merged

def write_bnet(output_file, merged_rules):
    """Write the merged rules to a .bnet file."""
    with open(output_file, 'w') as f:
        f.write("targets,factors\n")
        # Sort variables for consistent output
        for variable in sorted(merged_rules.keys()):
            f.write(f"{variable},{merged_rules[variable]}\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_rules_to_bnet.py <input_rules.txt> [output.bnet]")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    # Default output filename if not provided
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])
    else:
        output_file = input_file.parent / f"{input_file.stem}.bnet"
    
    # Parse rules
    rules_dict = parse_rules(input_file)
    
    # Merge rules for same variables
    merged_rules = merge_rules(rules_dict)
    
    # Write .bnet file
    write_bnet(output_file, merged_rules)
    
    print(f"Converted {len(merged_rules)} variables from '{input_file}' to '{output_file}'")

if __name__ == "__main__":
    main()
