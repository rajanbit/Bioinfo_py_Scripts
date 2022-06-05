from Bio.SeqUtils import GC
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

# Function to plot nucleotide composition
def nucl_comp(seq):
	nucl_dict = {"A": 0,  "T": 0, "G": 0, "C": 0}
	for nt in nucl_dict:
		nucl_dict[nt] = round((seq.count(nt)/len(seq))*100, 2)
	plt.bar(list(nucl_dict.keys()), list(nucl_dict.values()),
		color =['blue', 'red', 'green', 'orange'])

	plt.xlabel("Nucleotides")
	plt.ylabel("Percentage (%)")
	plt.title("Nucleotides Composition Plot")
	plt.savefig('nucleotide_composition.png',bbox_inches ="tight", pad_inches = 0.5)
	plt.close()
  
# Function to return GC composition
def gc_comp(seq):
	gc_perc = GC(seq)
	return("GC Percent:", round(gc_perc, 2))

# Function to plot codon composition
def codon_comp(seq):
	codons = [seq[x:x+3] for x in range(0, len(seq)+1, 3)]
	codon_dict = dict.fromkeys(list(set(codons)), 0)
	for codon in codon_dict:
		codon_dict[codon] = (codons.count(codon)/len(codons))*100
	codon_dict={key:value for key,value in codon_dict.items() if len(key)==3}
	plt.figure(figsize=(10,4))
	plt.bar(list(codon_dict.keys()), list(codon_dict.values()), color=get_cmap("Accent").colors)
	plt.xticks(fontsize=8, rotation=90)
	plt.xlabel("Codons")
	plt.ylabel("Percentage (%)")
	plt.title("Codons Composition Plot")
	plt.savefig('codon_composition.png',bbox_inches ="tight", pad_inches = 0.5, dpi = 500)
	plt.close()
