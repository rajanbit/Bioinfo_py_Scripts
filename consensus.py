#!/usr/bin/python
#!python

# import sys module
import sys
# import NumPy library 
import numpy as np

# file handling
f_file = sys.argv[1]
f_open = open(f_file, "r")
f_read = f_open.readlines()

# declaring variables
seq_list = []
seq = ""
header = ""

# assigning values to variables
for line in f_read:
	if ">" in line[0:1]:
		header = line[1:]
	elif ">" not in line[0:1]:
		seq += line.strip()
	seq_list.append(seq)
	seq = ""
seq_list = ' '.join(seq_list).split()

# calculating consensus
n = len(seq_list[0])
con_array = np.full((4, n), 0)
for seq in seq_list:
	for i, char in enumerate(seq):
		if char == "A":
			con_array[0][i] +=1
		elif char == "G":
			con_array[1][i] +=1
		elif char == "T":
			con_array[2][i] +=1
		elif char == "C":
			con_array[3][i] +=1

# printing output
print("A:",con_array[0],"\nG:",con_array[1],"\nT:",con_array[2],"\nC:",con_array[3])

# python consensus.py <multi_fasta_file>
