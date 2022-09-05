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