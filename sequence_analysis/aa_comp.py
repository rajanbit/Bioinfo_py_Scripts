# Importing modules
import sys
import pandas as pd
from Bio import SeqIO
import matplotlib.pyplot as plt

# Amino acid composition dict
aa_dict = { "nonpolar_aliphatic":["G", "A", "V", "L", "I", "P", "M"],
	    "nonpolar_aromatic":["F", "W"],
	    "polar_uncharged":["S", "T", "N", "Q", "C", "Y"],
	    "positive":["H", "K", "R"], "negative":["D", "E"], "NA":["-", "*"]}

# Reading Protein FASTA file 
data = SeqIO.parse(open(sys.argv[1]), "fasta")
seq = []
for record in data:
	seq.append(list(str(record.seq)))

# Creating dataframe containing aa comp infor for each seq
df = pd.DataFrame(columns = ["pos", "nonpolar_aliphatic", "nonpolar_aromatic","polar_uncharged", "positive", "negative", "NA"])
for i in range(len(seq[0])):
	temp = {"nonpolar_aliphatic":0, "nonpolar_aromatic":0,
		"polar_uncharged":0, "positive":0, "negative":0, "NA":0}
	for s in seq:
		temp["".join([j for j in aa_dict if s[i] in aa_dict[j]])] = temp["".join([j for j in aa_dict if s[i] in aa_dict[j]])]+1
	temp = { i:(temp[i]/sum(temp.values()))*100 for i in temp}
	temp["pos"] = i+1
	df.loc[len(df)]=temp

# Plotting stacked barplot
df.plot(x='pos', kind='bar', stacked=True, figsize=(15, 8))
plt.xlabel("Amino Acid Position")
plt.ylabel("Percentage(%)")
plt.legend(loc = "lower right")
plt.savefig('aa_composition_plot.png',bbox_inches ="tight", pad_inches = 0.1)
plt.close()

# Usage: python aa_comp.py aligned_seq.fasta
