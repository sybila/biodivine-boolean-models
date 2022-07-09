# \[078\] IMMUNE-SYSTEM

 - Variables: 151
 - Inputs: 13
 - Regulations: 506
 - Publication: https://doi.org/10.1186/1752-0509-6-96
 - Source: https://research.cellcollective.org/?dashboard=true#module/91515:1/immune-system-model/1
 - Keywords: cell-collective, curated, repaired


### Modifications

The regulatory graph was modified to ensure consistency with the update functions:

 - Regulation `Param_HealthyState10 (S_136) -> Param_HealthyState11 (S_100)` sign set to `unknown`.
 - Regulation `Cell_Treg_PF (S_77) -> Cell_NK_PF (S_113)` sign set to `unknown`.
 - Regulation `IL13 (S_65) -> Cell_Macrophage_Helminth (S_125)` marked as non-essential.
 - Regulation `IL4 (S_59) -> Cell_Macrophage_Helminth (S_125)` marked as non-essential.
 - Regulation `O2 (S_151) -> Merozoites_PF (S_132)` marked as non-essential.
 - Regulation `Cell_B_PF (S_138) -> Merozoites_PF (S_132)` sign set to `unknown`.
 - Regulation `NO (S_82) -> Merozoites_PF (S_132)` marked as non-essential.
 - Regulation `Cell_Th1_PF (S_133) -> Cell_Th1_PF (S_133)` sign set to `unknown`.
 - Regulation `Cell_CD4_Naive (S_49) -> PV_HIV (S_153)` sign set to `unknown`.
 - Regulation `Cell_CD8_Mtb (S_160) -> Rep_Mtb (S_154)` sign set to `unknown`.
 - Regulation `Cell_Th1_Mtb (S_105) -> Rep_Mtb (S_154)` sign set to `unknown`.
 - Regulation `Cell_CD8_Naive (S_155) -> Cell_CD8_Naive (S_155)` marked as non-essential.
 - Regulation `Cell_CD4_Naive (S_49) -> Cell_CD8_Mtb (S_160)` marked as non-essential.


### Model citation

```
@article{bbm-078,
  title={The cell collective: toward an open and collaborative approach to systems biology},
  author={Helikar, Tom{\'a}{\v{s}} and Kowal, Bryan and McClenathan, Sean and Bruckner, Mitchell and Rowley, Thaine and Madrahimov, Alex and Wicks, Ben and Shrestha, Manish and Limbu, Kahani and Rogers, Jim A},
  journal={BMC systems biology},
  volume={6},
  number={1},
  pages={1--14},
  year={2012},
  publisher={BioMed Central}
}

```

