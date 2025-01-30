from pathlib import Path

names = ["Akt","AP1","B9","Bach2","Bcl2","Bcl6","Bcl11b","BCR","Blimp1","CD4", 
	"CD8","CD19","CD122","Dll1","Ebf1","EOMES","ERK","ETS1","E2A","E4BP4",
	"Flt3","Flt3L","Foxo1","Foxp3","FR4","GATA3","Gfi1","Gzmb","HEB","HES1",
	"Helios","Hoxa9","ICOS","Id2","IFNb","IFNbR","IFNg","IFNgR","Ikaros","IL2",
	"IL2Ra","IL4","IL4R","IL6","IL6R","IL7","IL7R","IL10","IL10R","IL12",
	"IL12R","IL15","IL15Ra","IL17","IL18","IL18R","IL21","IL21R","IL23","IL23R",
	"IL27","IL27R","IRAK","Irf4","JAK1","JAK3","MAPK","NFkB","NFAT","Notch1",
	"Pax5","PDK1","Prf1","PU1","RORgt","Runx1","Runx3","SMAD2","SMAD3","SOCS1",
	"STAT1","STAT3","STAT4","STAT5","STAT6","Tbet","TCF1","TCR","TGFb","TGFbR",
	"ThPOK","TNFa","TNFR2","Tox2","XBP1"]

model = Path("source.txt").read_text().splitlines()

def l_min(*arg):
	return f"({' & '.join(arg)})"

def l_max(*arg):
	return f"({' | '.join(arg)})"

def l_not(x):
	return f"!{x}"

u = names

for line in model:
	target, function = line.split(";")	
	print(f"{target}, {eval(function)}")