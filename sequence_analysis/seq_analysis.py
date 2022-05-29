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
  
