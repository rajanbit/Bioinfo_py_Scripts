#!/usr/bin/python
#!python

import sys
import numpy as np

fasta_o = open(sys.argv[1], "r")
fasta_r = fasta_o.readlines()

seq_list = []
for line in fasta_r:
	if line[0] != ">" and line != "\n":
		seq_list.append(line.strip())

#Function
def frequency(base,total):
	try:
		f_base = base/total
	except ZeroDivisionError:
		f_base = 0
	return(f_base)
	
# Raw Frequency Matrix
n = len(seq_list[0])
m = 4
mat = np.full((m, n), 0.0)
for i in range(0,len(seq_list[0])):
	A = T = G = C = 0
	for data in seq_list:
		if data[i] == "A":
			A += 1
		elif data[i] == "G":
			G += 1
		elif data[i] == "T":
			T += 1
		elif data[i] == "C":
			C += 1
	tot = A+G+C+T

	fA = frequency(A,tot)
	fG = frequency(G,tot)
	fC = frequency(C,tot)
	fT = frequency(T,tot)

	mat[0,i] = fA
	mat[1,i] = fT
	mat[2,i] = fG
	mat[3,i] = fC

	A = T = G = C = 0

#Normalized Matrix
over_mat = mat.sum(axis = 1)/n
norm_mat = mat/over_mat[:,None]

#Convert Normalized Matrix to Log Odd Scores
scores = np.log2(norm_mat)
print(np.around(scores,decimals=2))

