# \[268\] COLORECTAL-CANCER-GSE1323

 - Variables: 156
 - Inputs: 47
 - Regulations: 501
 - Publication: https://doi.org/10.1101/2025.08.18.670822
 - Source: https://zenodo.org/record/7143340#.Yzx2L4RBwuU
 - Keywords: cellnetanalyzer, curated, multi-valued


### Modifications

The model is translated to .bnet using `convert_cellnetanalyzer_to_bnet.py`. Subsequently, the model has been converted to `.aeon` where
the following unused regulations were marked as non-essential:
 - AKT1_P has no effect in BAX.
 - CFLAR has no effect in CASP8.
 - CYCS has no effect in CASP9.
 - CDKN1A has no effect in CCND1.
 - CTNNB1_P_TCF_LEF1 has no effect in CCND1.
 - FOS_P has no effect in CCND1.
 - CTNNB1_P_TCF_LEF1 has no effect in CDH1_A.
 - SNAI1_A has no effect in CDH1_A.
 - TWIST1_A has no effect in CDH1_A.
 - CTNNB1_P_TCF_LEF1 has no effect in CDKN1A.
 - PRKCA has no effect in CDKN1A.
 - SMAD2_P_SMAD3_P_SAMD4 has no effect in CDKN1A.
 - TP53_P has no effect in CDKN1A.
 - SPHK1 has no effect in CERAMIDE.
 - MAPK14_P has no effect in CREBBP.
 - MSK1 has no effect in CREBBP.
 - SMAD2_P_SMAD3_P_SAMD4_N has no effect in CTNNB1_P_TCF_LEF1.
 - WNT5A_FZD1_P_LRP5_P_LRP6_P has no effect in DVL1_P.
 - MAPK14_P has no effect in ELK1_P_ATF2_P.
 - MAPK3_P has no effect in FOS_P.
 - PKCalpha_Ca2_PLUS has no effect in FOXC2.
 - PTGS2 has no effect in GSK3B_Axin2_P_APC_P_CTNNB_P_CHKA.
 - CREBBP has no effect in IL10.
 - DC has no effect in IL12A.
 - DC has no effect in IL6.
 - ESR2_P has no effect in IL6.
 - MAPK8_P has no effect in IL6.
 - MAPK3_P has no effect in JUN_P.
 - IL10 has no effect in MAC.
 - ROS has no effect in MAP2K1_P.
 - MAP3K1 has no effect in MAPK8_P.
 - MAP3K5 has no effect in MAPK8_P.
 - SMAD3_P has no effect in MAPK8_P.
 - ATM has no effect in MDM2.
 - CTNNB1_P_TCF_LEF1 has no effect in MDM2.
 - TP53_P has no effect in MDM2.
 - NFKB1_N has no effect in MMP2.
 - BAX has no effect in MOMP.
 - BCL2 has no effect in MOMP.
 - BID has no effect in MOMP.
 - PIK3CA_P has no effect in MTORC2.
 - CTNNB1_P_TCF_LEF1 has no effect in MYC.
 - STAT3_P_A has no effect in MYC.
 - CREBBP has no effect in NFKB1_N.
 - ESR1_n_P has no effect in NFKB1_N.
 - PTGER2 has no effect in PIK3CA_P.
 - RIP1 has no effect in PIK3CA_P.
 - SHC1_GRB2_SOS1_SRC has no effect in PIK3CA_P.
 - SMAD2_P_SMAD3_P has no effect in PIK3CA_P.
 - TNF_TNFRSF1B_TNFRSF1A has no effect in PIK3CA_P.
 - CERAMIDE has no effect in PPP2CB.
 - TNF_TNFRSF1B_TNFRSF1A has no effect in PTGS2.
 - CASP3 has no effect in Proliferation.
 - CDKN1A has no effect in Proliferation.
 - JUN_P has no effect in Proliferation.
 - SNAI2_A has no effect in Proliferation.
 - CASP3 has no effect in Proliferation_b3.
 - CDKN1A has no effect in Proliferation_b3.
 - SNAI2_A has no effect in Proliferation_b3.
 - CDKN1A has no effect in Proliferation_b4.
 - SNAI2_A has no effect in Proliferation_b4.
 - TNF_TNFRSF1B_TNFRSF1A has no effect in ROS.
 - TNF_TNFRSF1B_TNFRSF1A has no effect in SMPD1.
 - SMAD2_P_SMAD3_P_SAMD4_N has no effect in SNAI1_A.
 - NFKB1_N has no effect in SNAI2_A.
 - STAT3_P_A has no effect in SOD1.
 - MAPK3_P has no effect in STAT3_P_A.
 - MAPK8_P has no effect in TP53_P.
 - TP73_A has no effect in TP53_P.
 - TP53_P has no effect in TP73_A.
 - ZEB1_A has no effect in TP73_A.
 - IL10 has no effect in TREG.
 - SMAD2_P_SMAD3_P_SAMD4_N has no effect in TWIST1_A.
 - IFNG has no effect in Th1.
 - IL12A has no effect in Th1.
 - CTNNB1_P_TCF_LEF1 has no effect in VIM_A.
 - STAT3_P_A has no effect in VIM_A.
 - SNAI1_A has no effect in ZEB1_A.
 - SNAI2_A has no effect in ZEB1_A.
 - STAT6 has no effect in ZEB1_A.
 - TWIST1_A has no effect in ZEB1_A.
 - SNAI1_A has no effect in ZEB2_A.
 - SNAI2_A has no effect in ZEB2_A.
 - STAT6 has no effect in ZEB2_A.
 - TWIST1_A has no effect in ZEB2_A.


### Model citation

```
@article{bbm-268,
  title={Integrative network modeling of colorectal cancer reveals diagnostic signatures and therapeutic targets},
  author={Khan, Faiz M and Naveez, Muhammad and Salehzadeh-Yazdi, Ali and Rajendran, Vineetha and Wolkenhauer, Olaf and Gonzalez, Julio Vera},
  journal={bioRxiv},
  pages={2025--08},
  year={2025},
  publisher={Cold Spring Harbor Laboratory}
}

```

