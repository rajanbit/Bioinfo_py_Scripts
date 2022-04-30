#!/usr/bin/python
#!python

# Input and Read the Multi_FASTA record
import sys
file1 = sys.argv[1]
mlti_fasta = open(file1)
fasta_rec = mlti_fasta.readlines()
acc_list = []
for line in fasta_rec:
	if line[0] == ">":
		acc_list.append(line[1:10])

# Create Files with Accession_ids
def file_creater(acc_id):
	file_name = acc_id+".fasta"
	file_c = open(file_name,"w+")
	return(file_c)

# Writing FASTA records in Files
def file_writer(file_w, data):
	file_w.write(data)
	return(file_w)

# Parsing Multi_FASTA records
def parsing_data(acc_id, data):
	head_index = None
	seq = ""
	header = ""
	for i in range(0, len(data)):
		data_f = data[i]
		if acc_id in data_f:
			header += data_f
			head_index = i
			break
	if head_index != None:
		for i in range(head_index+1, len(data)):
			data_s = data[i]
			if data_s[0] != ">":
				seq += data_s
			else:
				break
	return(header+seq)

# Executing all the Functions
def out():
	for i in range(0, len(acc_list)):
		acc_id = acc_list[i]
		f1 = file_creater(acc_id)
		f2 = parsing_data(acc_id, fasta_rec)
		file_writer(f1, f2)
out()

# python multi_fasta_deconcatenator.py <Multi_FASTA_File>
