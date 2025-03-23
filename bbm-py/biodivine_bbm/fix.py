import os
from biodivine_aeon import BooleanNetwork
from pathlib import Path

file_format = None

def load_bn_file():
    with open("notes.md", "a") as notes:
        print("FIXED ERRORS:", file=notes)

    global file_format
    bn = None
    for file in os.listdir("./"):
        if file.endswith(".bnet"):
            file_format = 'bnet'
            file_content = Path(file).read_text()
            bn = BooleanNetwork.from_bnet(file_content)
        elif file.endswith(".aeon"):
            file_format = 'aeon'
            file_content = Path(file).read_text()
            bn = BooleanNetwork.from_aeon(file_content)
        elif file.endswith(".sbml"):
            file_format = 'sbml'
            file_content = Path(file).read_text()
            bn = BooleanNetwork.from_sbml(file_content)

        if bn:
            return bn

def erase_inputs(model: BooleanNetwork):
    for var in model.variables():
        if len(model.predecessors(var)) == 0:
            model.set_update_function(var, None)

    with open("notes.md", "a") as notes:
        print('Inputs', file=notes)

    return model

def erase_unused(bn):
    for var in bn.variables():
        if len(bn.predecessors(var)) == 0 and len(bn.successors(var)) == 0:
            bn = bn.drop(var)
    
    with open("notes.md", "a") as notes:
        print('Unused variables', file=notes)

    return bn

def fix_monotonicity_and_essentiality_mismatches(bn):
    with open("notes.md", "a") as notes:
        print("Monotonicity and essentiality", file=notes)

    return bn.infer_valid_graph()

def fix_incorrect_names(model):
    for var in model.variables():
        name = model.get_variable_name(var)
        model.set_variable_name(var, "v_"+name)

    with open("notes.md", "a") as notes:
        print("Incorrect names", file=notes)

    return model

def save_model(model):
    with open("notes.md", "a") as notes:
        print(file=notes)
    if file_format == 'bnet':
        Path('model.bnet').write_text(model.to_bnet())
    elif file_format == 'aeon':
        Path('model.aeon').write_text(model.to_aeon())
    elif file_format == 'sbml':
        Path('model.sbml').write_text(model.to_sbml())
    else:
        Path('model.bnet').write_text(model.to_bnet())
        Path('model.aeon').write_text(model.to_aeon())
        Path('model.sbml').write_text(model_to_aeon())
