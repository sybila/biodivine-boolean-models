# \[224\] BORTEZOMIB-PHARMACODYNAMIC-HETEROGENEITY

 - Variables: 87
 - Inputs: 8
 - Regulations: 210
 - Publication: https://doi.org/10.1124/jpet.118.247924
 - Source: https://github.com/ckadelka/DesignPrinciplesGeneNetworks/blob/02c847512151f43e1e74619b6f5e6c803c434b9c/update_rules_models_in_literature_we_randomly_come_across/29632237.txt
 - Keywords: grn-principles, curated, repaired


Obtained from the `grn-principles` dataset, as I can't seem to find the 
original model files.

### Modifications

The following regulations were adjusted to make the model logically consistent:

 - Regulation `PIP3 -> AKT` set as non-essential.
 - Regulation `BLIMP1 -> Bcl6` set as non-essential.
 - Regulation `mTORC1 -> DEPTOR` set as non-essential.
 - Regulation `mTORC2 -> DEPTOR` set as non-essential.
 - Regulation `DEPTOR -> mTORC1` set as non-essential.
 - Regulation `PRAS40 -> mTORC1` set as non-essential.
 - Regulation `DEPTOR -> mTORC2` set as non-essential.
 - Regulation `Prot -> pNFkB` set as non-essential.
 - Regulation `CDK2 -> pRB` set as non-essential.
 - Regulation `CYCB -> pRB` set as non-essential.
 - Regulation `IKK -> pSTAT3` set as non-essential.

### Model citation

```
@article{bbm-224,
  title={Network-based analysis of bortezomib pharmacodynamic heterogeneity in multiple myeloma cells},
  author={Ramakrishnan, Vidya and Mager, Donald E},
  journal={Journal of Pharmacology and Experimental Therapeutics},
  volume={365},
  number={3},
  pages={734--751},
  year={2018},
  publisher={ASPET}
}
```

