# \[244\] LIMPHOPOIESIS

 - Variables: 70
 - Inputs: 15
 - Regulations: 191
 - Publication: https://doi.org/10.1016/j.biosystems.2025.105399
 - Source: https://ars.els-cdn.com/content/image/1-s2.0-S0303264725000097-mmc2.zip
 - Keywords: curated, repaired


### Modifications

The model is derived from a julia simulation script, replacing min/max with AND/OR and 1-X with negation. The transformation was mostly manual with the help of regular expressions and `transform.py`. 

Removed unused variable: `Hoxa9`, `IL18`.

Variables changed to inputs: `IFNbR`, `IFNgR`, `IL10R`, `IL21R`, `IL23R`, `IL27R`, `IL6R`, `TGFbR`, `TNFR2`, `AP1`, `B9`, `BCR`, `Dll1`, `Flt3L`, `IFNb`, `IL2`, `IL7`, `IL12`, `IL15`, `IL21`, `IL23`, `IL27`, `TCR`.

### Model citation

```
@article{bbm-244,
  title={The regulatory network that controls lymphopoiesis},
  author={Mendoza, Luis and V{\'a}zquez-Ram{\'\i}rez, Ricardo and Tzompantzi-de-Ita, Juan Manuel},
  journal={BioSystems},
  pages={105399},
  year={2025},
  publisher={Elsevier}
}
```

