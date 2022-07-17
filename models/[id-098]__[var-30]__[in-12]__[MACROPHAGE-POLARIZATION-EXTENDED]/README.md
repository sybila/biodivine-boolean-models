# \[098\] MACROPHAGE-POLARIZATION-EXTENDED

 - Variables: 30
 - Inputs: 12
 - Regulations: 72
 - Publication: https://doi.org/10.3390/cancers12123664
 - Source: https://doi.org/10.3390/cancers12123664
 - Keywords: curated, repaired


### Modifications

The model is an extension of the BBM model number 94. Since the authors do not provide a complete model and only list the functions for new nodes, the model is based on `source.base-model.aeon`, which is the model number 94.

The rules again contain a bunch of typos and do not agree fully with the regulatory graph (e.g. `MCSF` is used instead of `MCSFR`, regulations for `STAT3` are incomplete, ...). On many functions, the operator priority is also very weird... a slight modifications of operator priority were made to better reflect the descriptions of the processes that the authors give in the paper (perhaps missing parentheses?).

TL;DR: This model was not easy to transform into anything machine readable, so please take it with a grain of salt.

### Model citation

```
@article{bbm-098,
  title={Insights on TAM formation from a Boolean model of macrophage polarization based on in vitro studies},
  author={Marku, Malvina and Verstraete, Nina and Raynal, Flavien and Madrid-Menc{\'\i}a, Miguel and Domagala, Marcin and Fourni{\'e}, Jean-Jacques and Ysebaert, Lo{\"\i}c and Poupot, Mary and Pancaldi, Vera},
  journal={Cancers},
  volume={12},
  number={12},
  pages={3664},
  year={2020},
  publisher={MDPI}
}
```

