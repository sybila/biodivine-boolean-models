# \[079\] COLORECTAL-TUMORIGENESIS

 - Variables: 184
 - Inputs: 13
 - Regulations: 747
 - Publication: https://doi.org/10.1186/s12918-016-0341-9
 - Source: https://doi.org/10.1186/s12918-016-0341-9
 - Keywords: curated, repaired


### Modifications

**Raw model:** The model is constructed from the published regulatory network (`source.links.tsv`) and logical truth tables (`source.truth_tables`) using the `build_model.py` script. The result is a `source.raw.aeon` file.

> `.aeon` format was chosen because the SBML description of a DNF encoded Boolean functions was very large (tens of megabytes).

File `source.links.tsv` is based on the original published table of links. However, note that this is not the "Additional file 1" which contains 688 links, but rather "Additional file 2", which contains (for some reason) substantially more regulations.

Still, several regulations had to be added in order to match the data in the truth tables. Namely:
 - `APC -? APC`
 - `beta_catenin -? APC`
 - `Integrins -? PTP1b`

Variable names containing `-` were also normalized to use `_` instead, and a some capitalisation typos were fixed.

**Additional repair:** Furthermore, in the final `source.aeon`, several modifications were performed to make the regulatory graph compatible with the published BN:

 - Regulation `Tpl2 -> NIK` marked as non-essential.
 - Regulation `PKC -> AC` marked as non-essential.
 - Regulation `PKA -> Src` marked as non-essential.
 - Regulation `bax -> bax` marked as non-essential.
 - Regulation `p38 -> p38` marked as non-essential.
 - Regulation `Smad2_4 -> MMP` sign set to `unknown`.
 - Regulation `PDK1 -> PAK` marked as non-essential.
 - Regulation `p120RasGAP -> Ras` marked as non-essential.
 - Regulation `ARF -> ARF` marked as non-essential.
 - Regulation `Rho -> PI5K` marked as non-essential.
 - Regulation `Rac -> PI5K` marked as non-essential.
 - Regulation `Ras -> Sos` marked as non-essential.
 - Regulation `PIP2_45 -> Sos` marked as non-essential.
 - Regulation `PAK -> Mek` marked as non-essential.
 - Regulation `bcl2 -> p53` marked as non-essential.
 - Regulation `RhoGDI -> Rho` sign set to `unknown`.
 - Regulation `PI3K -> PIP2_45` marked as non-essential.
 - Regulation `PLC_g -> PIP2_45` marked as non-essential.
 - Regulation `PLC_B -> PIP2_45` marked as non-essential.
 - Regulation `Src -> Fak` sign set to `unknown`.
 - Regulation `PTEN -> Fak` sign set to `unknown`.
 - Regulation `Trio -> Fak` sign set to `unknown`.
 - Regulation `Integrins -> PTP1b` marked as non-essential.
 - Regulation `PKC -> Talin` marked as non-essential.
 - Regulation `PTP1b -> EGFR` marked as non-essential.
 - Regulation `EGFR -> EGFR` marked as non-essential.
 - Regulation `Daxx -> ASK1` sign set to `unknown`.
 - Regulation `wip1 -> wip1` marked as non-essential.
 - Regulation `Ral -> PLD` marked as non-essential.
 - Regulation `atm -> rb` sign set to `unknown`.
 - Regulation `CyclinD -> rb` sign set to `unknown`.
 - Regulation `CyclinE -> rb` sign set to `unknown`.
 - Regulation `PKC -> GRK` marked as non-essential.
 - Regulation `PKC -> IP3R1` marked as non-essential.
 - Regulation `p53 -> cycg` sign set to `unknown`.
 - Regulation `RalBP1 -> Cdc42` marked as non-essential.
 - Regulation `p190RhoGAP -> Cdc42` marked as non-essential.
 - Regulation `Graf -> Cdc42` marked as non-essential.
 - Regulation `Akt -> Rac` marked as non-essential.
 - Regulation `Rho -> Rac` marked as non-essential.
 - Regulation `Src -> Csk` marked as non-essential.
 - Regulation `Fak -> Csk` marked as non-essential.
 - Regulation `p27 -> CyclinD` sign set to `unknown`.
 - Regulation `p15 -> CyclinD` sign set to `unknown`.
 - Regulation `p21 -> CyclinD` sign set to `unknown`.
 - Regulation `PP2A -> CaMK` marked as non-essential.
 - Regulation `PKA -> CaMKK` marked as non-essential.
 - Regulation `Src -> PP2A` marked as non-essential.
 - Regulation `cAMP -> PP2A` marked as non-essential.
 - Regulation `PP2A -> PP2A` marked as non-essential.
 - Regulation `Crk -> WASP` marked as non-essential.
 - Regulation `Akt -> p21` sign set to `unknown`.
 - Regulation `Myc -> p21` sign set to `unknown`.
 - Regulation `p53 -> p21` sign set to `unknown`.
 - Regulation `Smad2_4 -> p21` sign set to `unknown`.
 - Regulation `mdm2 -> p21` sign set to `unknown`.

### Model citation

```
@article{bbm-079,
  title={Attractor landscape analysis of colorectal tumorigenesis and its reversion},
  author={Cho, Sung-Hwan and Park, Sang-Min and Lee, Ho-Sung and Lee, Hwang-Yeol and Cho, Kwang-Hyun},
  journal={BMC systems biology},
  volume={10},
  number={1},
  pages={1--13},
  year={2016},
  publisher={Springer}
}
```

