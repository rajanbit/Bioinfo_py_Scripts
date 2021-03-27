#!/usr/bin/python

# Program to calculate protein molecular weight
# from the amino acid sequence in Fasta file

import sys

file_f = open(sys.argv[1], "r")
file_rl = file_f.readlines()
aa_mw = {"A":71.0779, "C":103.1429,"D":115.0874,"E":129.114,"F":147.1739,"G":57.0513,"H":137.1393,"I":113.1576,"K":128.1723,
"L":113.1576,"M":131.1961,"N":114.1026,"P":97.1152,"Q":128.1292,"R":156.1857,"S":87.0773,"T":101.1039,"V":99.1311,"W":186.2099,"Y":163.1733}


def calc(prot_seq, header):
	aa_molwt = 18.0153
	for i in range(0, len(prot_seq)):
		aa_molwt += aa_mw.get(prot_seq[i])

	print("Sequence Info: "+header[1:])
	print("Number of amino acid residues: "+str(len(prot_seq)))
	print("Protein molecular weight: "+str(round(aa_molwt/1000, 2))+" kDa ["+str(round(aa_molwt, 2))+" Da]\n")

seq = ""
head = ""
print("\nProtein Molecular Weight Calculator Result\n")
for line in file_rl:
	if line[0:1] == ">" and seq == "":
		head = line.strip()
	elif line[0:1] != ">":
		seq += line.strip()
	elif line[0:1] ==">" and seq != "":
		calc(seq, head)
		seq = ""
		head = line.strip()
calc(seq, head)

# Usage: python prot_mol_weight_calculator.py prot.fasta
