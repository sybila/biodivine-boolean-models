### Modifications

The model is derived from a julia simulation script, replacing min/max with AND/OR and 1-X with negation. The transformation was mostly manual with the help of regular expressions and `transform.py`. 

Removed unused variable: `Hoxa9`, `IL18`.

Variables changed to inputs: `IFNbR`, `IFNgR`, `IL10R`, `IL21R`, `IL23R`, `IL27R`, `IL6R`, `TGFbR`, `TNFR2`, `AP1`, `B9`, `BCR`, `Dll1`, `Flt3L`, `IFNb`, `IL2`, `IL7`, `IL12`, `IL15`, `IL21`, `IL23`, `IL27`, `TCR`.