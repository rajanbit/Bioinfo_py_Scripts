# Importing modules
from Bio.SeqUtils import GC
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from Bio.Seq import Seq
from Bio import SeqIO
import sys

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
	gc_dict = {"GC":gc_perc,"AT":100-gc_perc}
	plt.bar(list(gc_dict.keys()), list(gc_dict.values()), color =['blue', 'red'])
	plt.xticks(fontsize=8, rotation=90)
	plt.xlabel("Compositions")
	plt.ylabel("Percentage (%)")
	plt.title("GC & AT Composition Plot")
	plt.savefig('gc_at_composition.png',bbox_inches ="tight", pad_inches = 0.5, dpi = 500)
	plt.close()

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

# Function to plot amino acid composition
def aa_comp(seq):
	a_acid_seq = Seq(seq).translate()
	a_acid_seq = str(a_acid_seq).replace("*", "")
	a_acids = [ aa for aa in a_acid_seq]
	a_acids_dict = dict.fromkeys(list(set(a_acids)), 0)
	for aa in a_acids_dict:
		a_acids_dict[aa] = (a_acids.count(aa)/len(a_acids))*100
	plt.figure(figsize=(10,4))
	plt.bar(list(a_acids_dict.keys()), list(a_acids_dict.values()), color=get_cmap("tab20").colors)
	plt.xticks(fontsize=8, rotation=90)
	plt.xlabel("Amino Acids")
	plt.ylabel("Percentage (%)")
	plt.title("Amino Acid Composition Plot")
	plt.savefig('amino_acid_composition.png',bbox_inches ="tight", pad_inches = 0.5, dpi = 500)
	plt.close()

# Reading FASTA file and running all 
fasta_rec = open(sys.argv[1])
seq = ""
data = SeqIO.parse(fasta_rec, "fasta")
for record in data:
	seq = record.id, str(record.seq)
	seq = str(seq[1])
nucl_comp(seq)
gc_comp(seq)
codon_comp(seq)
aa_comp(seq)

# Usage: $ python orf_analyzer.py <seq.fasta>
