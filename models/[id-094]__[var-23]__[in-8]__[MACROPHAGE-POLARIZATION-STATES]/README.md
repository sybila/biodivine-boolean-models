# \[094\] MACROPHAGE-POLARIZATION-STATES

 - Variables: 23
 - Inputs: 8
 - Regulations: 52
 - Publication: https://doi.org/10.3389/fphys.2018.01659
 - Source: https://doi.org/10.3389/fphys.2018.01659
 - Keywords: curated, repaired


### Modifications

The model is originally published as a `.bnet` file, but the paper also contains information about regulations. As such, these were also added, resulting in an `.aeon` file.

The following regulations were also added because they are missing in the published list (some are visible in the main figure though - hence we know their monotonicity):
 - `IL1b -> IL1R`
 - `IL1b_e -> IL1R`
 - `IL10_out -> IL10R`
 - `PPARg -? PPARg`
 - `STAT6 -? STAT6`
 - `JMJD3 -? JMJD3`
 - `STAT3 -? STAT3`
 - `ERK -? ERK`

Finally, two regulations turned out to be non-essential:
 - Regulation `IL16_e -> IL1R` marked as non-essential.
 - Regulation `IL1b_e -> FcgR` marked as non-essential.

### Model citation

```
@article{bbm-094,
  title={Gene regulatory network modeling of macrophage differentiation corroborates the continuum hypothesis of polarization states},
  author={Palma, Alessandro and Jarrah, Abdul Salam and Tieri, Paolo and Cesareni, Gianni and Castiglione, Filippo},
  journal={Frontiers in physiology},
  volume={9},
  pages={1659},
  year={2018},
  publisher={Frontiers Media SA}
}
```

