### Modifications

The published model was not available at the time of publication. This model is a direct CaSQ translation of the `source.interaction.sbml` file, which is the interaction map.

Unused variables removed: `BSG`, `BTK_rna`, `DYNLRB1`, `HLA_DRB1_rna`, `HSPA5`, `IL1RN_rna`, `IL26`, `IL32_rna`, `IL33_rna`, `JUNB`, `MIR124A_rna`, `MIR203A_rna`, `MIR346_rna`, `MIR34A_rna`, `MK2_phosphorylated_M2_macrophage_nucleus`, `PDE4B`, `PDIA3_HLA_A_B2M_complex`.

The following regulations were set to non-essential to metch the update function semantics:
 - `TNFSF4_TNFRSF4_complex (csa465) -> TRAF2_TRAF5_TRAF6_complex_TH1___cytoplasm_active (csa490)`
 - `YY1 (sa873) -> MIR155_rna (sa798)`