### Availability

Honestly, I'm not quite sure where they found the rules, but they are available in the `grn-principles` dataset
and converted using `rules_to_bnet.py`. In order to be able to properly annotate the logical errors, we then 
covert the model to `.aeon`.

### Modifications

The following regulations were updated to fix logical inconsistencies:
 
 - Regulation `ATF2 -> AP1` set as non-essential.
 - Regulation `CRE -> AP1` set as non-essential.
 - Regulation `NUC_ERK1_2 -> AP1` set as non-essential.
 - Regulation `NUC_P38 -> AP1` set as non-essential.
 - Regulation `JNK -> BAD` set as non-essential.
 - Regulation `CALCIPRESSIN -> CALCINEURIN` set as non-essential.
 - Regulation `VAV -> CAM` set as non-essential.
 - Regulation `CBL -> FYN` set as non-essential.
 - Regulation `CD45 -> FYN` set as non-essential.
 - Regulation `AP1 -> GM_CSF` set as non-essential.
 - Regulation `IKK_GAMMA -> IKB_BETA` set as non-essential.
 - Regulation `TAK1_TAB -> IKK_GAMMA` set as non-essential.
 - Regulation `ETS -> IL2` set as non-essential.
 - Regulation `GSK3_BETA -> IL2` set as non-essential.
 - Regulation `GSK3_BETA -> IL4` set as non-essential.
 - Regulation `CBL -> LCK` set as non-essential.
 - Regulation `CD28 -> LCK` set as non-essential.
 - Regulation `CD45 -> LCK` set as non-essential.
 - Regulation `CABIN1 -> MEF2` set as non-essential.
 - Regulation `HDAC -> MEF2` set as non-essential.
 - Regulation `PKC -> NCK` set as non-essential.
 - Regulation `GSK3_BETA -> NUC_NFAT` set as non-essential.
 - Regulation `IL1 -> NUC_NFKB` set as non-essential.
 - Regulation `GRB7 -> RAS` set as non-essential.
 - Regulation `NCK_SOS -> RAS` set as non-essential.
 - Regulation `SHC_GRB2_SOS -> RAS` set as non-essential.
 - Regulation `SHP1_GRB2_SOS -> RAS` set as non-essential.
 - Regulation `SHP2_GRB2_GAB1_SOS -> RAS` set as non-essential.
 - Regulation `LYP -> ZAP70` set as non-essential.
 - Regulation `VAV -> ZAP70` set as non-essential.