### Modifications

The model is constructed based on the logical rules and regulations available in `source.raw.docx`. These are rewritten in a more structured format in `source.raw.regs.txt` and `source.raw.rules.txt`, where the variables are also renamed (eliminating `-` and `/`) to improve compatibility. Also, a few capitalization typos were fixed in the process. Using these files, `source.raw.aeon` is constructed. Finally, in the final `source.aeon`, we then also include some final modifications to make the logical rules and regulations compatible:
 
 - Regulation `Dest_compl -? Dest_compl` added.
 - Regulation `EMT -? EMT` added.
 - Regulation `GLI -? SHH` added.
 - Regulation `IGF1 -> SOS_GRB2` changed to `IGF1R -> SOS_GRB2`.
 - Regulation `Dest_Compl -> GSK3` marked as non-essential.
 - Regulation `catenin_nuc -> AXIN2` marked as non-essential.
 - Regulation `c_fos -> c_fos` marked as non-essential.
 - Regulation `Csl -> SNAI1` sign set to `unknown`.
 - Regulation `DELTA -> NOTCH` sign set to `unknown`.
 - Regulation `SNAI1 -> SNAI1` marked as non-essential.
 - Regulation `Csn -> GSK3` sign set to `unknown`.