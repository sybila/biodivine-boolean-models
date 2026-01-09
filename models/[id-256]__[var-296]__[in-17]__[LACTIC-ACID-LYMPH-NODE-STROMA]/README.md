# \[256\] LACTIC-ACID-LYMPH-NODE-STROMA

 - Variables: 296
 - Inputs: 17
 - Regulations: 1617
 - Publication: https://doi.org/10.1158/2326-6066.CIR-21-0778
 - Source: https://github.com/shorthouse-mrc/biomodelanalyzer_lactate/blob/master/Lactate_BioModelAnalyzer.json
 - Keywords: biomodelanalyzer, curated, multi-valued, repaired


### Modifications

Update function of `Complexes`, which is `(max((floor(var(223)/var(21))*var(223)),1))-(var(213)*2)` clearly contains division by zero if `var(21) = 0`. To avoid this, we replaced `var(21)` with `max(1, var(21))` in this particular case.

### Model citation

```
@article{bbm-256,
  title={Tumor-derived lactic acid modulates activation and metabolic status of draining lymph node stroma},
  author={Riedel, Angela and Helal, Moutaz and Pedro, Luisa and Swietlik, Jonathan J and Shorthouse, David and Schmitz, Werner and Haas, Lisa and Young, Timothy and da Costa, Ana SH and Davidson, Sarah and others},
  journal={Cancer immunology research},
  volume={10},
  number={4},
  pages={482--497},
  year={2022},
  publisher={American Association for Cancer Research}
}
```

