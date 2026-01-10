#!/usr/bin/env python3
"""
Convert CellNetAnalyzer reactions file to Boolean .bnet format using the second column as canonical.
- Parse reactions from second column (with coefficients)
- If reactant coefficient is 1, use variable as-is
- If reactant coefficient is N > 1, add suffix _bN to variable name
- Merge reactions with same product using | (or)
- Replace / and - in variable names with _
"""

from collections import defaultdict
import re
import sys

def normalize_variable_name(name):
    """Replace / and - with _ in variable names."""
    # Preserve negation symbol at the start
    if name.startswith('!'):
        return '!' + name[1:].replace('/', '_').replace('-', '_')
    return name.replace('/', '_').replace('-', '_')

def parse_canonical_reaction(second_col):
    """
    Parse reaction from second column format like:
    "1 CASP3 + 1 TP53_P = 2 Apoptosis"
    Returns: (list of (coeff, var_name) tuples for reactants, (coeff, product_name) for product)
    """
    if '=' not in second_col:
        return None, None
    
    reactants_str, product_str = second_col.split('=', 1)
    reactants_str = reactants_str.strip()
    product_str = product_str.strip()
    
    # Parse reactants: "1 VAR1 + 1 VAR2" or "1 !VAR1 + 2 VAR2"
    reactants = []
    # Match pattern: number followed by variable name (possibly with !)
    reactant_pattern = r'(\d+)\s+([!]?[A-Za-z0-9_/]+)'
    for match in re.finditer(reactant_pattern, reactants_str):
        coeff = int(match.group(1))
        var_name = match.group(2).strip()
        reactants.append((coeff, var_name))
    
    # Parse product: "2 Apoptosis" or "1 VAR"
    product_match = re.match(r'(\d+)\s+(.+)', product_str)
    if product_match:
        product_coeff = int(product_match.group(1))
        product_name = product_match.group(2).strip()
        return reactants, (product_coeff, product_name)
    
    return None, None

def convert_reactions_to_bnet(input_file, output_file):
    """Convert reactions file to bnet format using second column as canonical."""
    # Dictionary to store reactions grouped by product
    # Key: (product_coeff, normalized_product_name), Value: list of reactant expressions
    product_reactions = defaultdict(list)
    
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Split by tab and take second column (index 1)
            parts = line.split('\t')
            if len(parts) < 2:
                continue
            
            second_col = parts[1].strip()
            reactants, product = parse_canonical_reaction(second_col)
            
            if reactants is None or product is None:
                continue
            
            product_coeff, product_name = product
            normalized_product_name = normalize_variable_name(product_name)
            
            # For products, include the coefficient as part of the name (like "2Apoptosis")
            # If coefficient is 1, use name as-is; if > 1, prefix with the number
            if product_coeff == 1:
                product_key = normalized_product_name
            else:
                product_key = f'{normalized_product_name}_b{product_coeff}'
            
            # Process reactants with coefficients
            normalized_reactants = []
            for coeff, var_name in reactants:
                normalized_var = normalize_variable_name(var_name)
                
                # If coefficient is 1, use as-is; if > 1, add _bN suffix
                if coeff == 1:
                    normalized_reactants.append(normalized_var)
                else:
                    normalized_reactants.append(f'{normalized_var}_b{coeff}')
            
            # Join with & and add parentheses if multiple reactants
            if len(normalized_reactants) == 0:
                continue
            elif len(normalized_reactants) == 1:
                reactant_expr = normalized_reactants[0]
            else:
                reactant_expr = ' & '.join(normalized_reactants)
                reactant_expr = f'({reactant_expr})'
            
            product_reactions[product_key].append(reactant_expr)
    
    # Write bnet file
    with open(output_file, 'w') as f:
        f.write('targets, factors\n')
        
        # Sort products for consistent output
        for product in sorted(product_reactions.keys()):
            reactions = product_reactions[product]
            
            if len(reactions) == 1:
                # Single reaction
                f.write(f'{product}, {reactions[0]}\n')
            else:
                # Multiple reactions: join with |
                combined = ' | '.join(reactions)
                f.write(f'{product}, {combined}\n')

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = 'source.bnet'
    
    convert_reactions_to_bnet(input_file, output_file)
    print(f'Converted {input_file} to {output_file}')
