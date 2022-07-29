# \[207\] BREAST-CANCER-TUMOUR

 - Variables: 85
 - Inputs: 18
 - Regulations: 441
 - Publication: https://doi.org/10.3389/fdata.2021.656395
 - Source: https://github.com/Domenico321/attractors-search/blob/57a429c7a204a70096a8f802ab1887e28c6ec9d9/attractor.py
 - Keywords: curated, repaired


### Modifications

The model is constructed automatically from the regulations list. Every function states that *some* activator must be present and no inhibitor must be present in order to activate. As such, we don't need to state the actual regulations because they are clearly correct.

The presented model is actually based on the model available on github, but we merge the two update functions of the `RELA` node in order to follow the rule stated above.

### Model citation

```
@article{bbm-207,
	title={Data-Driven Modeling of Breast Cancer Tumors Using Boolean Networks},
	author={Sgariglia, Domenico and Conforte, Alessandra Jordano and Pedreira, Carlos Eduardo and de Carvalho, Luis Alfredo Vidal and Carneiro, Flavia Raquel Gon{\c{c}}alves and Carels, Nicolas and da Silva, Fabricio Alves Barbosa},
	journal={Frontiers in big Data},
	volume={4},
	year={2021},
	publisher={Frontiers Media SA}
}
```

