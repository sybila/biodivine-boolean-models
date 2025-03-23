from biodivine_aeon import *

bn = BooleanNetwork(["a", "b", "c"])
bn.ensure_regulation({
  'source': 'a',
  'target': 'b',
  'sign': '+',
  'essential': True
})

bn.ensure_regulation({
  'source': 'b',
  'target': 'a',
  'sign': None,
  'essential': True
})

bn.ensure_regulation({
    'source': 'b',
    'target': 'b',
    'sign': '+',
    'essential': True
})

bn.set_update_function('b', '(a ^ b)')
print(bn.to_sbml())

bn.set_update_function('a', '!b')
bn.set_update_function('b', '(a ^ b)')

valid = bn.infer_valid_graph()

print(bn.find_regulation('b', 'a')['sign'], valid.find_regulation('b', 'a')['sign'])
print(bn.find_regulation('b', 'b')['sign'], valid.find_regulation('b', 'b')['sign'])
 
