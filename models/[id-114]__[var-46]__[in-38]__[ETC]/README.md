# \[114\] ETC

 - Variables: 46
 - Inputs: 38
 - Regulations: 154
 - Publication: https://doi.org/10.1038/s41597-020-0477-8
 - Source: https://git-r3lab.uni.lu/covid/models/-/blob/4ed915a55687f626f9e7b3d4ada249cbaa5945b8/Executable%20Modules/SBML_qual_build/sbml/ETC_stable.sbml
 - Keywords: covid-disease-map, curated, casq, repaired


### Modifications

Variable `Nsp5 (sa693)` removed becuase it is not connected to the rest of the network. Additionally, the regulatory graph was modified to ensure consistency with the update functions:

 - Regulation `O_2__simple_molecule (sa24) -> H__ion_mitochondrion (sa18)` marked as non-essential.
 - Regulation `sa13_Cyt_C_mitochondrial_matrix (sa13) -> H__ion_mitochondrion (sa18)` marked as non-essential.
 - Regulation `sa255_QH_2__simple_molecule_mitochondrial_matrix (sa255) -> H__ion_mitochondrion (sa18)` marked as non-essential.
 - Regulation `paraquat_simple_molecule (sa397) -> superoxide_simple_molecule (sa354)` marked as non-essential.


### Model citation

```
@article{bbm-114,
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

