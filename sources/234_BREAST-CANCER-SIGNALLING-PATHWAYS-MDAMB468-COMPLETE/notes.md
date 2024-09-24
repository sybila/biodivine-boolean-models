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

as the analysis stated that TEAD1 and TCF4 have no effect on CYCLIN_D_c.
