# Clustal Omega to FASTA

import sys
import re

msa_open = open(sys.argv[1], "r")
msa_fast = open(sys.argv[2], "w+")
msa_rl = msa_open.readlines()

s_char = ["*",":"]

temp_l = []
head_l = []
for line in msa_rl:
	line = line.strip()

	if "CLUSTAL" in line:
		pass
		
	elif line == "":
		pass

	elif line == "\n":
		pass

	else:
		m = re.search(r'\d+$', line)

		if m is not None:
			line = line.split("\t")
			line = re.sub("\s\s+", ",",line[0])
			line = line.split(",")
			temp_l.append(line) 
			head_l.append(line[0])

head_l = list(set(head_l))

for head in head_l:
	msa_fast.write(">"+head+"\n")
	for data in temp_l:
		if head in data:
			msa_fast.write(data[1]+"\n")

# python clustal_to_fasta.py <file.clustal_num> <file.fasta>
