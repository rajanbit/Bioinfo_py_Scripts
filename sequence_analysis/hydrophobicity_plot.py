#!/usr/bin/python
#!python


# Python script for calculating and plotting
# hydrophobicity of a given peptide/protein 
# sequence using Kyte-Doolittle scale


# Importing modules
import sys
from Bio import SeqIO
import matplotlib.pyplot as plt

# Kyte-Doolittle scale
kydo = { 'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
	'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
	'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
	'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2 }

x_plot = []
y_plot = []

# Function for converting sequence to Kyte-Doolittle propensity
def seq_to_kydo(seq):
	kydo_values = []
	for aa in seq:
		kydo_values.append(kydo[aa])
	return(kydo_values)

# Function for smoothing the data 
def smoothing(values_list):
	window = int(9) # Adjust window size here
	half_window = int((window-1)/2)
	new_values = [0]*half_window+values_list+[0]*half_window
	y = [] # Smoothened Kyte-Doolittle Values
	x = [] # Amino acid positions
	for i in range(half_window,len(new_values)-half_window):
		y.append(sum(new_values[i-half_window:i+1+half_window])/window)
	for j in range(1, len(values_list)+1):
		x.append(j)
	return(x, y)

# Reading fasta record
fasta_rec = open(sys.argv[1])
seq_data = SeqIO.parse(fasta_rec, "fasta")
for record in seq_data:
	header, sequence = record.id, str(record.seq)
	x_plot, y_plot = smoothing(seq_to_kydo(sequence))[0], smoothing(seq_to_kydo(sequence))[1]

# Plotting the data
plt.plot(x_plot, y_plot)
plt.title("Kyte-Doolittle Hydrophobicity Plot")
plt.xlabel("Amino Acid Position")
plt.ylabel("Hydrophobicity Score")
plt.savefig('hydrophobicity_plot.png',bbox_inches ="tight", pad_inches = 0.5, dpi = 500)
plt.close()


# Usage: python hydrophobicity_plot.py prot.fasta
