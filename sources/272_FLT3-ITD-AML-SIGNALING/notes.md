### Modifications

The model is taken from a different paper (https://github.com/IlyaLab/LogicModelMerger/tree/main) where it was translated to SBML. The original model files are also
available (https://github.com/SaccoPerfettoLab/FLT3-ITD_driven_AML_Boolean_models/tree/main), but are only listed in some R-specific format, so taking the SBML
was much easier. Also note that there are many versions of the model, as this is intended as patient-specific model. As such, this is only one possible version
among all presented models.

Also, the .sbml model contained some syntax errors in update functions of model inputs `PTPN1`, `KIT`, `TNF`, `IGF1R`, `PDPK1`. These have been updated such that
the input variable simply has no transition object.

Furthermore, dual regulations have been declared as two regulations (`MAP2K1 -> FLT3`, `PIK3CA -> MAP2K1`, `TSC2 -> PTEN`). These have been changed to dual, as per SBML spec.

Update functions of `RPS6`, `RPS6KA1`, `PTPN11`, `KRAS` and `RPS6KB1` contained doubly-nested `<apply>` which has been removed.

Finally, the following regulations were marked as non-essential:
 - TNF has no effect in FLT3.
 - MAPK8 has no effect in FLT3.
 - MAP2K1 has no effect in FLT3.
 - STAT3 has no effect in FLT3.
 - IGF1R has no effect in FLT3.
 - MAP2K1 has no effect in MAPK1.
 - FLT3 has no effect in MAPK14.
 - PIK3CA has no effect in MAP2K1.
 - MTOR has no effect in MAP2K1.
 - RPS6KB1 has no effect in MAP2K1.
 - IGF1R has no effect in IRS1.
 - PTPN1 has no effect in IRS1.
 - CBL has no effect in INSR.
 - KIT has no effect in GRB2.
 - GSK3B has no effect in PTEN.
 - CREB1 has no effect in PTEN.
 - TSC2 has no effect in PTEN.
 - RPS6KB1 has no effect in PTEN.
 - RPS6 has no effect in PTEN.
 - GSK3B has no effect in TSC2.
 - GSK3B has no effect in CREB1.