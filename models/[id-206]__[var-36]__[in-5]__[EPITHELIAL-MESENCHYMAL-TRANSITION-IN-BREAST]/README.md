# \[206\] EPITHELIAL-MESENCHYMAL-TRANSITION-IN-BREAST

 - Variables: 36
 - Inputs: 5
 - Regulations: 97
 - Publication: https://doi.org/10.1038/s41467-017-00268-2
 - Source: https://sourceforge.net/projects/e2f1map/files/
 - Keywords: curated, repaired


### Modifications

The model is constructed from the given reaction list. Note that the output `EMT` node is technically multivalued, but this does not play due to it being an output, we thus only provide a Boolean abstraction. Note that regulation info is also available as part of the original publication (however, only as a larger network). We do not include it explicitly because the logical rules are created semi-automatically anyway - i.e. we do not expect to be an error in translation.

Finally, regulation from `snai2` to `emt` has been marked as non-essential because it has no effect (this could be due to the Booleanization of `emt` though).

### Model citation

```
@article{bbm-206,
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

