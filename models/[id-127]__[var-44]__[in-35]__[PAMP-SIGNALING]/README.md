# \[127\] PAMP-SIGNALING

 - Variables: 44
 - Inputs: 35
 - Regulations: 109
 - Publication: https://doi.org/10.1038/s41597-020-0477-8
 - Source: https://git-r3lab.uni.lu/covid/models/-/blob/4ed915a55687f626f9e7b3d4ada249cbaa5945b8/Executable%20Modules/SBML_qual_build/sbml/PAMP_signaling_stable.sbml
 - Keywords: covid-disease-map, curated, casq, repaired


### Modifications

Variables `RIPK1 (sa421)`, `ubiquitin_proteasome_complex_complex (csa87)` removed becuase they are not connected to the rest of the network. Additionally, the regulatory graph was modified to ensure consistency with the update functions:

 - Regulation `Orf3b (sa356) -> IRF3_phosphorylated_cell (sa119)` marked as non-essential.
 - Regulation `Orf8 (sa355) -> IRF3_phosphorylated_cell (sa119)` marked as non-essential.
 - Regulation `Nsp3 (sa349) -> IRF3_phosphorylated_cell (sa119)` marked as non-essential.



### Model citation

```
@article{bbm-127,
  title={COVID-19 Disease Map, building a computational repository of SARS-CoV-2 virus-host interaction mechanisms},
  author={Ostaszewski, Marek and Mazein, Alexander and Gillespie, Marc E and Kuperstein, Inna and Niarakis, Anna and Hermjakob, Henning and Pico, Alexander R and Willighagen, Egon L and Evelo, Chris T and Hasenauer, Jan and others},
  journal={Scientific data},
  volume={7},
  number={1},
  pages={1--4},
  year={2020},
  publisher={Nature Publishing Group}
}

```

