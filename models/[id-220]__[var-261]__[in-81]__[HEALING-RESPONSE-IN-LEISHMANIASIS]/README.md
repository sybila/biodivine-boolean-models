# \[220\] HEALING-RESPONSE-IN-LEISHMANIASIS

 - Variables: 261
 - Inputs: 81
 - Regulations: 748
 - Publication: https://doi.org/10.1186/s13637-015-0032-7
 - Source: https://github.com/ckadelka/DesignPrinciplesGeneNetworks/blob/02c847512151f43e1e74619b6f5e6c803c434b9c/update_rules_models_in_literature_we_randomly_come_across/26660865.txt
 - Keywords: grn-principles, curated, repaired


### Availability

The model is given as a `.booleannet` file in the supplement of the paper. However, here we use the 
version available in the "GRN principles" dataset as it is already translated to a machine-readable
format. The format is then translated to `.bnet` using `rules_to_bnet.py` script.

Since the model also contains a lot of logical issues, the files is then translated from `.bnet`
to `.aeon`, where we can add annotations to indicate that these are accounted for.

### Modifications

The following modifications were made to make the model logically consistent with it's regulatory graph:

 - Regulation `ATF2_T -> AP1_T` set as non-essential.
 - Regulation `CRE_T -> AP1_T` set as non-essential.
 - Regulation `NUC_ERK1_2_T -> AP1_T` set as non-essential.
 - Regulation `NUC_P38_T -> AP1_T` set as non-essential.
 - Regulation `JNK_T -> BAD_T` set as non-essential.
 - Regulation `BCLX_S_T -> BCLX_T` set as non-essential.
 - Regulation `CALCIPRESSIN_T -> CALCINEURIN_T` set as non-essential.
 - Regulation `VAV_T -> CAM_T` set as non-essential.
 - Regulation `FASLS_T -> FASL_T` set as non-essential.
 - Regulation `CBL_T -> FYN_T` set as non-essential.
 - Regulation `CD45_T -> FYN_T` set as non-essential.
 - Regulation `IKK_ALPHA_T -> IKB_ALPHA_T` set as non-essential.
 - Regulation `ETS_T -> IL2_T` set as non-essential.
 - Regulation `IFN_GAMMA_T -> IL2_T` set as non-essential.
 - Regulation `IL4_SHORT_T -> IL4_T` set as non-essential.
 - Regulation `NUC_NFKB_T -> IL6_DELTA4_T` set as non-essential.
 - Regulation `NUC_NFKB_T -> IL6_NATIVE_T` set as non-essential. 
 - Regulation `IL6_DELTA4_T -> IL6_T` set as non-essential.
 - Regulation `CBL_T -> LCK_T` set as non-essential.
 - Regulation `CD28_T -> LCK_T` set as non-essential.
 - Regulation `CD45_T -> LCK_T` set as non-essential.
 - Regulation `CABIN1_T -> MEF2_T` set as non-essential.
 - Regulation `HDAC_T -> MEF2_T` set as non-essential. 
 - Regulation `PKC_T -> NCK_T` set as non-essential.
 - Regulation `BCL10_T -> NFKB_T` set as non-essential.
 - Regulation `CARMA1_T -> NFKB_T` set as non-essential.
 - Regulation `IKK_ALPHA_T -> NFKB_T` set as non-essential.
 - Regulation `IKK_GAMMA_T -> NFKB_T` set as non-essential.
 - Regulation `MALT1_T -> NFKB_T` set as non-essential.
 - Regulation `OX40L -> NFKB_T` set as non-essential.
 - Regulation `OX40_T -> NFKB_T` set as non-essential.
 - Regulation `PKC_THETA_T -> NFKB_T` set as non-essential.
 - Regulation `RIP1_T -> NFKB_T` set as non-essential.
 - Regulation `TRAF2_T -> NFKB_T` set as non-essential.
 - Regulation `CD40 -> NUC_ERK1_2` set as non-essential.
 - Regulation `FC_GAMMAR -> NUC_ERK1_2` set as non-essential.
 - Regulation `IGG -> NUC_ERK1_2` set as non-essential.
 - Regulation `TRAF6 -> NUC_ERK1_2` set as non-essential.
 - Regulation `CD40 -> NUC_P38` set as non-essential.
 - Regulation `TRAF2 -> NUC_P38` set as non-essential.
 - Regulation `TRAF3 -> NUC_P38` set as non-essential.
 - Regulation `TRAF5 -> NUC_P38` set as non-essential.
 - Regulation `GRB7_T -> RAS_T` set as non-essential.
 - Regulation `NCK_plus_SOS_T -> RAS_T` set as non-essential.
 - Regulation `SHC_plus_GRB2_plus_SOS_T -> RAS_T` set as non-essential.
 - Regulation `SHP1_plus_GRB2_plus_SOS_T -> RAS_T` set as non-essential.
 - Regulation `SHP2_plus_GRB2_plus_GAB1_plus_SOS_T -> RAS_T` set as non-essential.
 - Regulation `IL12 -> STAT4_T` set as non-essential.
 - Regulation `IL12R_T -> STAT4_T` set as non-essential.
 - Regulation `LYP_T -> ZAP70_T` set as non-essential.
 - Regulation `VAV_T -> ZAP70_T` set as non-essential.





### Model citation

```
@article{bbm-220,
  title={Identification of Th1/Th2 regulatory switch to promote healing response during leishmaniasis: a computational approach},
  author={Ganguli, Piyali and Chowdhury, Saikat and Chowdhury, Shomeek and Sarkar, Ram Rup},
  journal={Eurasip Journal on Bioinformatics and Systems Biology},
  volume={2015},
  number={1},
  pages={1--19},
  year={2015},
  publisher={Springer}
}
```

