# \[237\] COLORECTAL-TUMORIGENESIS-REVERSION-SWITCH

 - Variables: 17
 - Inputs: 0
 - Regulations: 44
 - Publication:  https://doi.org/10.1002/advs.202412503
 - Source: https://advanced.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fadvs.202412503&file=advs10563-sup-0003-TableS2.csv
 - Keywords: curated


### Modifications

The model is based on a list of functions provided as a `.csv` file. This `.csv` file is manually transformed into a `.bnet` model.

Afterwards, the following modifications were made to ensure logical consistency with the regulatory graph:
 - `NFIL3 -> DDIT3` was set to non-essential.
 - `MAFF -> KLF6` was set to non-essential.
 - `SREBF1 -> NFIA` was set to non-essential.

### Model citation

```
@article{bbm-237,
  title={Attractor Landscape Analysis Reveals a Reversion Switch in the Transition of Colorectal Tumorigenesis},
  author={Shin, Dongkwan and Gong, Jeong-Ryeol and Jeong, Seoyoon D and Cho, Youngwon and Kim, Hwang-Phill and Kim, Tae-You and Cho, Kwang-Hyun},
  journal={Advanced Science},
  pages={2412503},
  year={2024},
  publisher={Wiley Online Library}
}
```

