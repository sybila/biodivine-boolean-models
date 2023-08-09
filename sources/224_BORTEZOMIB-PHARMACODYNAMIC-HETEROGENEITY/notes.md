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