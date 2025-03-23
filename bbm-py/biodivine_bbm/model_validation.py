from biodivine_aeon import BooleanNetwork, AsynchronousGraph
from typing import Dict, Set
import re
from pathlib import Path
import biodivine_aeon as aeon

# v sync.py sa pouziva check_integrity -> ma nam toto sluzit na detekciu chyb typu "other"?

############################
# stahovanie modelov zo CellCollective a BioModels


# Common types of errors:
#  - Variable is unused
#  - Variable is an input
#  - Regulation monotonicity mismatch
#  - Regulation essentiality mismatch
#  - Other
#  - Dangerous variable name (does not match [a-z][A-Z0-9_]*)

# Automatic fixing script - generated function calls by some fixing script
# Validation errors, automatic fixes should be dumped into notes, if there is manual fix, the file has to be edited manually
#


# https://biodivine.fi.muni.cz/docs/aeon-py/latest/biodivine_aeon.html

def validate_model(bn: BooleanNetwork):
    errors = {}
    errors['Unused variables'] = check_for_unused_variables(bn)
    errors['Input variables'] = check_for_input_variables(bn)
    mismatches = check_for_monotonicity_and_essentiality_mismatch(bn)
    errors['Monotonicity mismatch'] = mismatches[0]
    errors['Essentiality mismatch'] = mismatches[1]
    errors['Incorrect names'] = check_for_incorrect_variable_names(bn)
    errors['Others'] = check_integrity(bn)
    with open('notes.md', 'a') as report_file:
        print('MODEL VALIDATION RESULTS:', file=report_file)
        report_errors(errors, report_file, bn)
        print(file=report_file)


def report_errors(errors, report_file, bn):
    with open("fix_script.py", "w") as fix_script:
        print("import fix", file=fix_script)
        print(file=fix_script)
        print("bn = fix.load_bn_file()", file=fix_script)
        for key in errors.keys():
            error_message = f'INFO {key}: OK'
            if errors[key] and key != 'Others':
                values = ', '.join(str(value) for value in errors[key])
                error_message = f'ERROR {key}: {values}'
                generate_fix_script(key, values, fix_script, bn)
            if key == 'Others' and not errors[key]:
                error_message = f'ERROR {key}: NOK'
            print(error_message)
            print(error_message, file=report_file)
        print("fix.save_model(bn)", file=fix_script)


def generate_fix_script(key, values, fix_script, bn):
    if key == 'Unused variables':
        print("bn = fix.erase_unused(bn)", file=fix_script)
    elif key == 'Input variables':
        print("bn = fix.erase_inputs(bn)", file=fix_script)
    elif key == 'Monotonicity mismatch' or key == 'Essentiality mismatch':
        print("bn = fix.fix_monotonicity_and_essentiality_mismatches(bn)", file=fix_script)
    elif key == 'Incorrect names':
        print("bn = fix.fix_incorrect_names(bn)", file=fix_script)


def check_for_unused_variables(bn):
    unused = set()
    for var in bn.variables():
        if len(bn.predecessors(var)) == 0 and len(bn.successors(var)) == 0:
            unused.add(bn.get_variable_name(var))
    return unused


def check_for_input_variables(bn):
    inputs = set()
    for var in bn.variables():
        function = bn.get_update_function(var)
        if function and function.as_var() == var and len(bn.predecessors(var)) <= 1:
            inputs.add(bn.get_variable_name(var))
    return inputs


def check_for_monotonicity_and_essentiality_mismatch(bn):
    # infer_valid_graph -> comparing regulations from the old and the new graph
    mismatched_monotonicity = set()
    essentiality_mismatch = set()
    inferred_graph = bn.infer_valid_graph()
    for original_regulation in bn.regulations():
        orig_reg_source = original_regulation['source']
        orig_reg_target = original_regulation['target']
        orig_reg_sign = original_regulation['sign']
        reg = inferred_graph.find_regulation(orig_reg_source, orig_reg_target)
        if not reg:
            essentiality_mismatch.add(f"({bn.get_variable_name(orig_reg_source)}, {bn.get_variable_name(orig_reg_target)})")
        elif orig_reg_sign != reg['sign']:
            mismatched_monotonicity.add(f"({bn.get_variable_name(reg['source'])}, {bn.get_variable_name(reg['target'])})")

    return (mismatched_monotonicity, essentiality_mismatch)


def check_integrity(bn):
    try:
        async_graph = AsynchronousGraph(bn)
    except:
        return False
    return async_graph.network_variable_count() == bn.variable_count()

def check_for_incorrect_variable_names(bn):
    incorrect_names = set()
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]*$'
    for var in bn.variables():
        name = bn.get_variable_name(var)
        if not re.match(pattern, name):
            incorrect_names.add(name)
    return incorrect_names


def tests():
    #aeon_test = """<?xml version='1.0' encoding='UTF-8' standalone='no'?><sbml xmlns="http://www.sbml.org/sbml/level3/version1/core" layout:required="false" level="3" qual:required="true" xmlns:layout="http://www.sbml.org/sbml/level3/version1/layout/version1" version="1" xmlns:qual="http://www.sbml.org/sbml/level3/version1/qual/version1"><model><qual:listOfQualitativeSpecies xmlns:qual="http://www.sbml.org/sbml/level3/version1/qual/version1"><qual:qualitativeSpecies qual:maxLevel="1" qual:constant="false" qual:name="a" qual:id="a"/><qual:qualitativeSpecies qual:maxLevel="1" qual:constant="false" qual:name="b" qual:id="b"/><qual:qualitativeSpecies qual:maxLevel="1" qual:constant="false" qual:name="c" qual:id="c"/></qual:listOfQualitativeSpecies><qual:listOfTransitions xmlns:qual="http://www.sbml.org/sbml/level3/version1/qual/version1"><qual:transition qual:id="tr_a"><qual:listOfInputs><qual:input qual:qualitativeSpecies="b" qual:transitionEffect="none" qual:sign="positive" qual:id="tr_a_in_b" essential="true"/></qual:listOfInputs><qual:listOfOutputs><qual:output qual:qualitativeSpecies="a" qual:transitionEffect="assignmentLevel" qual:id="tr_a_out"/></qual:listOfOutputs></qual:transition><qual:transition qual:id="tr_b"><qual:listOfInputs><qual:input qual:qualitativeSpecies="a" qual:transitionEffect="none" qual:sign="positive" qual:id="tr_b_in_a" essential="true"/></qual:listOfInputs><qual:listOfOutputs><qual:output qual:qualitativeSpecies="b" qual:transitionEffect="assignmentLevel" qual:id="tr_b_out"/></qual:listOfOutputs></qual:transition><qual:transition qual:id="tr_c"><qual:listOfInputs></qual:listOfInputs><qual:listOfOutputs><qual:output qual:qualitativeSpecies="c" qual:transitionEffect="assignmentLevel" qual:id="tr_c_out"/></qual:listOfOutputs></qual:transition></qual:listOfTransitions></model></sbml>"""
    #aeon_test = """<?xml version='1.0' encoding='UTF-8' standalone='no'?><sbml xmlns="http://www.sbml.org/sbml/level3/version1/core" layout:required="false" level="3" qual:required="true" xmlns:layout="http://www.sbml.org/sbml/level3/version1/layout/version1" version="1" xmlns:qual="http://www.sbml.org/sbml/level3/version1/qual/version1"><model><qual:listOfQualitativeSpecies xmlns:qual="http://www.sbml.org/sbml/level3/version1/qual/version1"><qual:qualitativeSpecies qual:maxLevel="1" qual:constant="false" qual:name="a" qual:id="a"/><qual:qualitativeSpecies qual:maxLevel="1" qual:constant="false" qual:name="b" qual:id="b"/><qual:qualitativeSpecies qual:maxLevel="1" qual:constant="false" qual:name="c" qual:id="c"/></qual:listOfQualitativeSpecies><qual:listOfTransitions xmlns:qual="http://www.sbml.org/sbml/level3/version1/qual/version1"><qual:transition qual:id="tr_a"><qual:listOfInputs><qual:input qual:qualitativeSpecies="b" qual:transitionEffect="none" qual:sign="unknown" qual:id="tr_a_in_b" essential="true"/></qual:listOfInputs><qual:listOfOutputs><qual:output qual:qualitativeSpecies="a" qual:transitionEffect="assignmentLevel" qual:id="tr_a_out"/></qual:listOfOutputs></qual:transition><qual:transition qual:id="tr_b"><qual:listOfInputs><qual:input qual:qualitativeSpecies="a" qual:transitionEffect="none" qual:sign="positive" qual:id="tr_b_in_a" essential="true"/><qual:input qual:qualitativeSpecies="b" qual:transitionEffect="none" qual:sign="positive" qual:id="tr_b_in_b" essential="true"/></qual:listOfInputs><qual:listOfOutputs><qual:output qual:qualitativeSpecies="b" qual:transitionEffect="assignmentLevel" qual:id="tr_b_out"/></qual:listOfOutputs><qual:listOfFunctionTerms><qual:defaultTerm qual:resultLevel="0"/><qual:functionTerm qual:resultLevel="1"><math xmlns="http://www.w3.org/1998/Math/MathML"><apply><xor/><apply><eq/><ci>a</ci><cn type="integer">1</cn></apply><apply><eq/><ci>b</ci><cn type="integer">1</cn></apply></apply></math></qual:functionTerm></qual:listOfFunctionTerms></qual:transition><qual:transition qual:id="tr_c"><qual:listOfInputs></qual:listOfInputs><qual:listOfOutputs><qual:output qual:qualitativeSpecies="c" qual:transitionEffect="assignmentLevel" qual:id="tr_c_out"/></qual:listOfOutputs></qual:transition></qual:listOfTransitions></model></sbml>"""
    aeon_test = Path("model.sbml").read_text()
    test_bn = BooleanNetwork.from_sbml(aeon_test)
    validate_model(test_bn)


if __name__ == '__main__':
    tests()
