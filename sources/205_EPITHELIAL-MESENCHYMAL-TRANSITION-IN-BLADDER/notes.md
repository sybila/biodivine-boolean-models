### Modifications

The model is constructed from the given reaction list. Note that the output `EMT` node is technically multivalued, but this does not play due to it being an output, we thus only provide a Boolean abstraction. Note that regulation info is also available as part of the original publication (however, only as a larger network). We do not include it explicitly because the logical rules are created semi-automatically anyway - i.e. we do not expect to be an error in translation.

Furthermore, following regulations were updated as non-essential because they do not have impact on the outcomes of the respective update functions (althugh note that for `EMT` this might be due to the Boolean abstraction):
 - `axin2 -> ctnnb1`
 - `mir_200b_3p -> emt`
 - `smad2 -> emt`
 - `smad4 -> emt`
 - `snai1 -> emt`
 - `smad2 -> myc`
 - `smad2 -> sp1`