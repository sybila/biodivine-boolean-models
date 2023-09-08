from pathlib import Path
from biodivine_aeon import *

# Note that the methods assume that the model is in the "canonical" format,
# i.e. with all inputs as free.

def inputs_free(model):
	return model

def inputs_constant(model, constant):
	for var in model.variables():
		if len(model.graph().regulators(var)) == 0:
			model.set_update_function(var, constant)
	return model

def inputs_identity(model):
	# For identity, we have to also add self-regulations to inputs.
	new_rg = model.graph()
	for var in model.variables():
		if len(model.graph().regulators(var)) == 0:
			new_rg.add_regulation({
				'source': var, 
				'target': var, 
				'observable': True, 
				'monotonicity': "activation"
			})

	new_model = BooleanNetwork(new_rg)
	for var in model.variables():
		if len(model.graph().regulators(var)) == 0:
			new_model.set_update_function(var, model.get_variable_name(var))
		else:
			new_model.set_update_function(var, model.get_update_function(var))

	return new_model

def output_model(dir, model, id, format, suffix = ""):
	if format == "aeon":
		Path(f"{dir}/{id:03d}{suffix}.aeon").write_text(model.to_aeon())
	if format == "bnet":
		Path(f"{dir}/{id:03d}{suffix}.bnet").write_text(model.to_bnet())
	if format == "sbml":
		Path(f"{dir}/{id:03d}{suffix}.sbml").write_text(model.to_sbml())
