import os
import sys
file_in = sys.argv[1]
os.system("cp "+file_in+" tempoxc1265.fasta")

name_list = ["ECO","SAL"]
for name in name_list:
	cmd = "sed -i "+"'/"+name+"/c\>"+name+"' tempoxc1265.fasta"
	os.system(cmd)
fasta_f = open("tempoxc1265.fasta", "r")
file_out = open ("concatenated_seq.fasta","w+")
fast = fasta_f.readlines()
l = []
new = []
for line in fast:
	if line not in l and line[0] == ">":
		new.append(line)
		l.append(line)
	elif line[0] != ">":
		new.append(line)
	else:
		pass
for line in new:
	file_out.write(line)
os.system("rm tempoxc1265.fasta")
file_out.close()

# python seq_concatenator.py <file.fasta>
