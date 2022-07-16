### Modifications

The model is manually constructed based on "Table S2", which contains the regulation edges with monotonicity annotations, and "Text S2" which contains the update functions for each variable. The transformation was performed manually, since the amount of data is not particularly substantial and the datasets contain a lot of typos and small errors (some variables use two names depending on context, a lot of capitalisation is just randomly changed, etc.). The names of variables were also normalized to ensure compatibility. This produced the file `source.raw.aeon`.

To make the regulatory graph and update functions consistent, the following modifications had to be performed:
 - A `RCN1 -? RBOH` regulation was added.
 - A `PtdInsP4 -? PtdIns_4_5_P2` regulation was added.
 - A `Vacuolar_Acidification -? Vacuolar_Acidification` regulation was added.
 - Regulation `pHc -> pHc` marked as non-essential.
 - Regulation `PtdInsP4 -> Aquaporin_PIP2_1` marked as non-essential.
 - Regulation `RCN1 -> ROS` marked as non-essential.
 - Regulation `S1P_PhytoS1P -> S1P_PhytoS1P` marked as non-essential. 

Finally, variables `AGB1`, `AGG3`, and `ROP10` were removed completely, because they do not have update functions specified in the original paper and only serve as network outputs. (If you want to include them, you can always take the relevant regulations from the `source.raw.aeon` file and add your own update functions)