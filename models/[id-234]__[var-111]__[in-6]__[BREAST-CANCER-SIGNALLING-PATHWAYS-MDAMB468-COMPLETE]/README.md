# \[234\] BREAST-CANCER-SIGNALLING-PATHWAYS-MDAMB468-COMPLETE

 - Variables: 111
 - Inputs: 6
 - Regulations: 271
 - Publication: https://doi.org/10.1371/journal.pone.0298788
 - Source: https://github.com/Ktaoma/BoolSyn
 - Keywords: source (?), curated (?), repaired (?), multi-valued (?)


### Modifications

Removed regulations:
PG, PG
NRG1, NRG1
INS, INS
ES, ES
EGF, EGF
DLL_i, DLL_i

Regulation:

CYCLIN_D_c, (((TEAD1 | TCF4 | STAT3) & !(GSK3B & (CDKN2A & P21)))) & (EIF4E & MYC & STAT3)

was updated to:

CYCLIN_D_c, (((STAT3) & !(GSK3B & (CDKN2A & P21)))) & (EIF4E & MYC & STAT3)

as the analysis


### Model citation

```
@article{bbm-234,
	author = {Taoma, Kittisak and Ruengjitchatchawalya, Marasri and Liangruksa, Monrudee and Laomettachit, Teeraphan},
	year = {2024},
	doi = {https://doi.org/10.1371/journal.pone.0298788},
	title = {Boolean modeling of breast cancer signaling pathways uncovers mechanisms of drug synergy},
	publisher = {PLOS ONE}
}


```

