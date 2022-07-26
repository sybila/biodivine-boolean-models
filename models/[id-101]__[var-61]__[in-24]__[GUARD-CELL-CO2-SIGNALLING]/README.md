# \[101\] GUARD-CELL-CO2-SIGNALLING

 - Variables: 61
 - Inputs: 24
 - Regulations: 155
 - Publication: https://doi.org/10.1093/plphys/kiab344
 - Source: https://github.com/dyhe-2000/Boolink-GUI/blob/5ac7ec9649e3dec17d7ebdcd9940941841154733/sample_data_files/ABA_CO2_data_files/Stomata2-0/Boolean%20Equations%20in%20words%20Stomata2-0.txt
 - Keywords: curated, boolink, repaired


### Modifications

The model should be an extension of network number 84 (`ABA INDUCED STOMATAL CLOSURE`). The model was downloaded from the tool repository in a format similar to `.bnet` (i.e. without regulation info). Technically, the regulation info may be available in the main manuscript, but I do not have time to read the whole paper. Also, constant update functions for `ABA`, `CO2`, `GTP`, `Sph`, `SCAB1`, `RCN1`, `DAGK`, `CPK6`, `CPK23`, `PtdInsP3`, `PtdInsP4`, `PC`, `Nitrite`, `GCR1`, `NADPH`, `NAD`, `MRP5`, `GAPC`, `ERA1`, `ABH1`, `ARP23`, `NtSyp121`, `NtSyp121`, and `SPP1` were removed to turn them into proper inputs.

### Model citation

```
@article{bbm-101,
	title={Boolink: a graphical interface for open access Boolean network simulations and use in guard cell CO2 signaling},
	author={Karanam, Aravind and He, David and Hsu, Po-Kai and Schulze, Sebastian and Dubeaux, Guillaume and Karmakar, Richa and Schroeder, Julian I and Rappel, Wouter-Jan},
	journal={Plant Physiology},
	volume={187},
	number={4},
	pages={2311--2322},
	year={2021},
	publisher={Oxford University Press}
}
```

