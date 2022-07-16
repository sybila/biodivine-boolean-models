# \[087\] INFLAMMATORY-GENE-EXPRESSION-IN-MACROPHAGES

 - Variables: 99
 - Inputs: 34
 - Regulations: 190
 - Publication: https://doi.org/10.1371/journal.pcbi.1005018
 - Source: https://doi.org/10.1371/journal.pcbi.1005018
 - Keywords: curated, repaired


### Modifications

The model is published as a list of reactions (`source.raw.txt`). The final update rules are then manually constructed as disjunctions of individual reactions (with each reaction being a conjunction). Since this format does not include information about regulation monotonicity, we use `.bnet` to represent the model. Some variables were renamed to ensure compatibility with other software. Also, some typos were found (e.g. `IRS-1/2` vs. `IRS1/2`) and hopefully fixed.

### Model citation

```
@article{bbm-087,
  title={Model-based characterization of inflammatory gene expression patterns of activated macrophages},
  author={Rex, Julia and Albrecht, Ute and Ehlting, Christian and Thomas, Maria and Zanger, Ulrich M and Sawodny, Oliver and H{\"a}ussinger, Dieter and Ederer, Michael and Feuer, Ronny and Bode, Johannes G},
  journal={PLoS computational biology},
  volume={12},
  number={7},
  pages={e1005018},
  year={2016},
  publisher={Public Library of Science San Francisco, CA USA}
}
```

