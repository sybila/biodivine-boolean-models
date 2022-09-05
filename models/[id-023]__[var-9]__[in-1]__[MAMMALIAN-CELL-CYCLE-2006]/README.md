# \[023\] MAMMALIAN-CELL-CYCLE-2006

 - Variables: 9
 - Inputs: 1
 - Regulations: 34
 - Publication: https://doi.org/10.1093/bioinformatics/btl210
 - Source: ['https://research.cellcollective.org/?dashboard=true#module/2396:1/mammalian-cell-cycle-2006/1', 'http://ginsim.org/node/4']
 - Keywords: cell-collective, ginsim, curated, repaired


### Modifications

To ensure network inputs are canonically represented, the auto-regulated identity update function of `CycD (S_5)` has been removed.

Additionally, the following regulations were modified to ensure consistency of update functions with the regulatory graph:

 - Regulation `UbcH10 (S_10) -> CycA (S_7)` sign set to `unknown`.
 - Regulation `CycE (S_2) -> p27 (S_9)` sign set to `unknown`.

### Model citation

```
@article{bbm-023,
  title={Dynamical analysis of a generic {Boolean} model for the control of the mammalian cell cycle},
  author={Faur{\'e}, Adrien and Naldi, Aur{\'e}lien and Chaouiya, Claudine and Thieffry, Denis},
  journal={Bioinformatics},
  volume={22},
  number={14},
  pages={e124--e131},
  year={2006},
  publisher={Oxford University Press}
}
```

