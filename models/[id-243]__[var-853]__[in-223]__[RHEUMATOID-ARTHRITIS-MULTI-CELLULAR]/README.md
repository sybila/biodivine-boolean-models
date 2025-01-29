# \[243\] RHEUMATOID-ARTHRITIS-MULTI-CELLULAR

 - Variables: 853
 - Inputs: 223
 - Regulations: 1807
 - Publication: https://doi.org/10.1038/s41746-024-01396-y
 - Source: https://www.ebi.ac.uk/biomodels/MODEL2408030001
 - Keywords: biomodels, curated, repaired, casq


### Modifications

The published model was not available at the time of publication. This model is a direct CaSQ translation of the `source.interaction.sbml` file, which is the interaction map.

Unused variables removed: `BSG`, `BTK_rna`, `DYNLRB1`, `HLA_DRB1_rna`, `HSPA5`, `IL1RN_rna`, `IL26`, `IL32_rna`, `IL33_rna`, `JUNB`, `MIR124A_rna`, `MIR203A_rna`, `MIR346_rna`, `MIR34A_rna`, `MK2_phosphorylated_M2_macrophage_nucleus`, `PDE4B`, `PDIA3_HLA_A_B2M_complex`.

The following regulations were set to non-essential to metch the update function semantics:
 - `TNFSF4_TNFRSF4_complex (csa465) -> TRAF2_TRAF5_TRAF6_complex_TH1___cytoplasm_active (csa490)`
 - `YY1 (sa873) -> MIR155_rna (sa798)`

### Model citation

```
@article{bbm-243,
  title={Building a modular and multi-cellular virtual twin of the synovial joint in Rheumatoid Arthritis},
  author={Zerrouk, Naouel and Aug{\'e}, Franck and Niarakis, Anna},
  journal={npj Digital Medicine},
  volume={7},
  number={1},
  pages={379},
  year={2024},
  publisher={Nature Publishing Group UK London}
}
```

