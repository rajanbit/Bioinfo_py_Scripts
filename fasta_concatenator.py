#!/usr/bin/python
#!python

# Extracting files name with the extension .fasta
import os
def get_name():
	f_fasta = []
	root = os.getcwd()
	for files in os.listdir(root):
		if files.endswith(".fasta"):
			f_fasta.append(files)
	return(f_fasta)

# Concatenating all the fasta files to create multi_fasta file
def concatenate():
	f_out = open("multi_fasta", "w+")
	f_file = get_name()
	for data in f_file:
		fasta_rec = open(data, "r")
		for lines in fasta_rec:
			f_out.write(lines)
concatenate()
