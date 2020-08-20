#!/usr/bin/python

# Extracts Fasta_records from Multi_Fasta file
# whose ids are in Accession_Ids file

import sys
file1 = sys.argv[1] # MULTI_FASTA File
file2 = sys.argv[2] # ACCESSION_IDS File
acc_id = open(file2, "r")
mlti_fasta = open(file1, "r")
out_fasta = open("output.fasta", "w+")
acc_list = []
for line in acc_id:
	acc_list.append(line.strip())
seq =""
for line in mlti_fasta:
	if line[0] == ">" and seq == "":
		header = line
	elif line[0]!= ">":
		seq += line
	elif line[0] == ">" and seq != "":
		for i in acc_list:
			if i in header:
				out_fasta.write(header + seq)
		seq = ""
		header = line
if i in header:
	out_fasta.write(header + seq)
