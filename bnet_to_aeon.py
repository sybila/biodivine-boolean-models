from biodivine_aeon import *
import sys

bn = BooleanNetwork.from_file(sys.argv[1])
print(bn.to_aeon())