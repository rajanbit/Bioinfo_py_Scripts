#!/usr/bin/python
#!python

# Importing Modules
import sys
from Bio import SeqIO


# Function for Overlapping Kmers
def overlapping_kmer_constructor(seq):
	if len(sys.argv[2].split("..")) == 1:
		k = int(sys.argv[2])
		for i in range(len(seq)):
	        	print(seq[i:i+k])

	elif len(sys.argv[2].split("..")) > 1:
		k_list = sys.argv[2].split("..")
		k_list = [i for i in range(int(k_list[0]), int(k_list[1])+1)]
		for k in k_list:
			k = int(k)
			for i in range(len(seq)):
				print(seq[i:i+k])

# Function for Non-Overlapping Kmers
def nonoverlapping_kmer_constructor(seq):
	if len(sys.argv[2].split("..")) == 1:
		k = int(sys.argv[2])
		for i in range(0, len(seq), k):
			print(seq[i:i+k])

	elif len(sys.argv[2].split("..")) > 1:
		k_list = sys.argv[2].split("..")
		k_list = [i for i in range(int(k_list[0]), int(k_list[1])+1)]
		for k in k_list:
			k = int(k)
			for i in range(0, len(seq), k):
				print(seq[i:i+k])


# Reading Fasta Records
fasta_in = open(sys.argv[1])
fasta_recs = SeqIO.parse(fasta_in, "fasta")
for rec in fasta_recs:
	head, seq = rec.id, str(rec.seq)
	
	# Generating Overlapping Kmers
	if sys.argv[3] == "-O":
		overlapping_kmer_constructor(seq)
	
	# Generating Non-Overlapping Kmers
	elif sys.argv[3] == "-N":
		nonoverlapping_kmer_constructor(seq)
		
# Usage: $ python kmer_constructor-1.py a.fasta 3/3..7 -N/-O
