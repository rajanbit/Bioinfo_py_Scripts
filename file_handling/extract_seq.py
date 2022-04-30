#!/usr/bin/python

# Program to extract nucleotide or protein
# sequence of particular index from a Fasta file

import sys

file_db = open(sys.argv[1], "r")

head = ""
seq = ""
fasta_seq = ""

for line in file_db:
	if line[0:1] == ">" and seq == "":
		head = line
	elif line[0:1] != ">":
		seq += line.strip()
	elif line[0:1] == ">" and seq != "":
		print("Multi FASTA record found ...\nProgram Break ...\n")
		quit()

index_b = int(input("Enter the sequence index [FROM]: "))
index_e = int(input("Enter the sequence index [TO]: "))
print("Sequence index: "+str(index_b)+"..."+str(index_e))

dot_in = head.index(".")
out_head = head[:dot_in+2]+":"+str(index_b)+"-"+str(index_e)+head[dot_in+2:]
out_seq = seq[index_b-1:index_e]
for i in range(0, len(out_seq), 70):
	fasta_seq += out_seq[i:i+70]+"\n"
print(out_head+fasta_seq)

file_out = open(head[1:dot_in+2]+"_out.fasta","w")
file_out.write(out_head+fasta_seq)

print("Saving sequence ... Done\nFile: "+head[1:dot_in+2]+"_out.fasta\n")
