### Availability

The model is available as list of polynomials. To the best of my knowledge, these 
should be interpreted as "modulo two". Under this assumption, every +1 is a negation
and every * is a conjunction. As such, the rules were updated manually to reflect this
and create a `.bnet` network. 

I am not sure what `* *` means. I am interpreting it as a conjunction with a typo.
If it is exponentiation, God help us all.

### Modifications

Variable `NKX3.1` renamed to `NKX3_1`, and generally changed all `-` in variable names to `_`.

Removed identity update functions on `ADAM17`, `CK2`, `Cdc37`, `EBP1`, `EpCAM`, `ERG`, `FHL2`, `IL_4`, `KAT5`, `MED15`, `MTUS1`, `PKIB`, `PTEN`, `RAC1`, `RhoGAP`, `SIAH2`, `SKIP`, `TMPRSS2`, `TRAP6`, `Vav3`, `Wnt` and `Znt4` to make them canonical inputs.

Finally, regulation `Cdc37 -> AR` has been marked as non-essential.