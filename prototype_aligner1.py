# importing modules
import sys
import numpy as np

# Function for Alignment
def Aligner():
	n=len(seq1)
	m=len(seq2)
	matrix = np.full((n, m), 0)
	for i in range(0,n):
		for j in range(0, m):
			if seq1[i] == seq2[j]:
				matrix[i,j] = 1
			else:
				matrix[i,j] = 0

	al_seq = ""
	for x in range(0, m):
		if matrix[x,x] == 1:
			al_seq += seq1[x]
		elif matrix[x,x] == 0:
			al_seq += "-"

	fast_al_seq = ""
	for y in range(0, len(al_seq), 70):
		fast_al_seq += al_seq[y:y+70]+"\n"
	print(">Aligned Sequence")
	print(fast_al_seq)

# Accessory code
seq1=""
seq2=""
mf_file = sys.argv[1]
mf_open = open(mf_file, "r")
mf_read = mf_open.readlines()
l1= []
for id_index, line in enumerate(mf_read, 1):
	if ">" in line:
            l1.append(id_index)
seq1_temp = mf_read[l1[0]: l1[1]-1]
seq2_temp = mf_read[l1[1]:]
for data1 in seq1_temp:
	seq1 += data1.strip()
for data2 in seq2_temp:
	seq2 += data2.strip()

Aligner()

# Usage: python prototype_aligner1.py <file.fasta> 
