#!/usr/bin/python

# Extract Fasta_record from Multi_Fasta file
# whose Accession_no is inputted by the user and
# write the record in a new file (NC_XXXXXX.fasta)

import os
import sys
file1 = sys.argv[1] # MULTI_FASTA File
mlti_fasta = open(file1)
lines = mlti_fasta.readlines()
acc_id = input("Enter the Accession_No: ")
f_name = acc_id+".fasta"
file2 = open(f_name,"w+")
head_index = None
for i in range(0, len(lines)):
	data = lines[i]
	if acc_id in data:
		file2.write(data)
		head_index = i
		break
if head_index != None:
	for i in range(head_index+1, len(lines)):
		data = lines[i]
		if data[0] != ">":
			file2.write(data)
		else:
			break
	file2.close()
else:
	print("Error: FASTA record not found")
	os.remove(f_name)
