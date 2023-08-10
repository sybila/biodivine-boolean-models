# \[005\] FA-BRCA-PATHWAY

 - Variables: 28
 - Inputs: 0
 - Regulations: 123
 - Publication: https://doi.org/10.1093/bioinformatics/bts036
 - Source: https://research.cellcollective.org/?dashboard=true#module/1778:1/fa-brca-pathway/1
 - Keywords: cell-collective, grn-principles, curated, repaired


### Modifications

The following changes have been made to make sure the regulatory graph is consistent with the network's update functions:

 - Regulation `FAcore (S_17) -> PCNATLS (S_5)` set as non-essential.
 - Regulation `FANCD2I (S_4) -> MRN (S_8)` sign set to `unknown`.
 - Regulation `ATR (S_27) -> NHEJ (S_9)` sign set to `unknown`.
 - Regulation `ssDNARPA (S_16) -> NHEJ (S_9)` sign set to `unknown`.
 - Regulation `FAN1 (S_28) -> XPF (S_20)` sign set to `unknown`.
 - Regulation `FANCD2I (S_4) -> XPF (S_20)` sign set to `unknown`.


### Model citation

```
@article{bbm-005,
  title={A Boolean network model of the {FA/BRCA} pathway},
  author={Rodriguez, Alfredo and Sosa, David and Torres, Leda and Molina, Bertha and Frias, Sara and Mendoza, Luis},
  journal={Bioinformatics},
  volume={28},
  number={6},
  pages={858--866},
  year={2012},
  publisher={Oxford University Press}
}
```

