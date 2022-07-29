# \[205\] EPITHELIAL-MESENCHYMAL-TRANSITION-IN-BLADDER

 - Variables: 41
 - Inputs: 4
 - Regulations: 118
 - Publication: https://doi.org/10.1038/s41467-017-00268-2
 - Source: https://sourceforge.net/projects/e2f1map/files/
 - Keywords: curated, repaired


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

### Model citation

```
@article{bbm-205,
	title={Unraveling a tumor type-specific regulatory core underlying E2F1-mediated epithelial-mesenchymal transition to predict receptor protein signatures},
	author={Khan, Faiz M and Marquardt, Stephan and Gupta, Shailendra K and Knoll, Susanne and Schmitz, Ulf and Spitschak, Alf and Engelmann, David and Vera, Julio and Wolkenhauer, Olaf and P{\"u}tzer, Brigitte M},
	journal={Nature communications},
	volume={8},
	number={1},
	pages={1--15},
	year={2017},
	publisher={Nature Publishing Group}
}
```

