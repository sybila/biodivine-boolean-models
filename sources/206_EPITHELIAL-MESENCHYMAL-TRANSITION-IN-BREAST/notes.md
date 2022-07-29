### Modifications

The model is constructed from the given reaction list. Note that the output `EMT` node is technically multivalued, but this does not play due to it being an output, we thus only provide a Boolean abstraction. Note that regulation info is also available as part of the original publication (however, only as a larger network). We do not include it explicitly because the logical rules are created semi-automatically anyway - i.e. we do not expect to be an error in translation.

Finally, regulation from `snai2` to `emt` has been marked as non-essential because it has no effect (this could be due to the Booleanization of `emt` though).