from pathlib import Path
from biodivine_aeon import *
import copy

# Note that the methods assume that the model is in the "canonical" format,
# i.e. with all inputs as free.

def inputs_free(model):
	return copy.copy(model)

def inputs_constant(model: BooleanNetwork, constant: bool):
	model = copy.copy(model)
	for var in model.variables():
		if len(model.predecessors(var)) == 0:
			model.set_update_function(var, UpdateFunction.mk_const(model, constant))
	return model

def inputs_identity(model: BooleanNetwork):
	# For identity, we have to also add self-regulations to inputs.
	new_model = copy.copy(model)
	for variable in new_model.variables():
		if len(new_model.predecessors(variable)) == 0:
			reg: IdRegulation = { 'source': variable,
				'target': variable,
				'essential': True,
				'sign': '+'
			}
			new_model.ensure_regulation(reg)
			new_model.set_update_function(variable, UpdateFunction.mk_var(new_model, variable))

	return new_model

def output_model(dir: str, model: BooleanNetwork, id: int, format: str, suffix: str = ""):
	if format == "aeon":
		Path(f"{dir}/{id:03d}{suffix}.aeon").write_text(model.to_aeon())
	if format == "bnet":
		Path(f"{dir}/{id:03d}{suffix}.bnet").write_text(model.to_bnet())
	if format == "sbml":
		Path(f"{dir}/{id:03d}{suffix}.sbml").write_text(model.to_sbml())
	if format == "bma":
		Path(f"{dir}/{id:03d}{suffix}.bma.json").write_text(model.to_bma_json(pretty=True))
	if format == "booleannet":
		Path(f"{dir}/{id:03d}{suffix}.booleannet.txt").write_text(model.to_booleannet())