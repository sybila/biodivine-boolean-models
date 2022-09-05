# \[140\] BREAST-CANCER-DRUG-RESISTANCE

 - Variables: 62
 - Inputs: 18
 - Regulations: 211
 - Publication: https://doi.org/10.1186/s41236-017-0007-6
 - Source: https://github.com/jgtz/BreastCancerModelv2/blob/e018f50344b378e57f36ba9fcceda6611f2a71b8/Models/BreastCancerModel_ZanudoEtAl2017.booleannet
 - Keywords: curated


### Modifications

The model is only available as `.booleannet` file with no regulation data. It was then manually converted to `.bnet`. Finally, constant update functions for variables `Alpelisib`, `Fulvestrant`, `Everolimus`, `Trametinib`, `Ipatasertib`, `Palbociclib`, `Neratinib`, `HER2`, `IGF1R_T`, `HER3_T`, `PDK1`, `SGK1_T`, `PIM`, `PTEN`, `BIM_T`, `BCL2_T`, `ER`, and `PBX1` were removed to make them canonical inputs.

### Model citation

```
@article{bbm-140,
	title={A network modeling approach to elucidate drug resistance mechanisms and predict combinatorial drug treatments in breast cancer},
	author={G{\'o}mez Tejeda Za{\~n}udo, Jorge and Scaltriti, Maurizio and Albert, R{\'e}ka},
	journal={Cancer convergence},
	volume={1},
	number={1},
	pages={1--25},
	year={2017},
	publisher={Springer}
}
```

