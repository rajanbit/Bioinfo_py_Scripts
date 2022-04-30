# Base Compositions of DNAs from Multi/Fasta Record

import sys

f_file = sys.argv[1]
file_op = open(f_file, "r")
lines = file_op.readlines()
file_wr = open("base_composition.tsv", "w+")
file_wr.write("DNA origin	A	T	G	C	Length	AT%	GC%\n")
seq = ""
head = ""
for line in lines:
	if line[0] == ">" and seq == "":
		head = line
	elif line[0]!= ">":
		seq += line.strip()
	elif line[0] == ">" and seq != "":

			file_wr.write(str(head[1:12])+"\t"+str(seq.count("A"))+"\t"+str(seq.count("T"))+\
"\t"+str(seq.count("G"))+"\t"+str(seq.count("C"))+"\t"+str(len(seq))+"\t"+"%.2f" %(((seq.count("A")+seq.count("T"))/len(seq))*100)+"\t"\
+"%.2f" %(((seq.count("G")+seq.count("C"))/len(seq))*100)+"\t"+"\n")
			seq = ""
			head = line

file_wr.write(str(head[1:12])+"\t"+str(seq.count("A"))+"\t"+str(seq.count("T"))+\
"\t"+str(seq.count("G"))+"\t"+str(seq.count("C"))+"\t"+str(len(seq))+"\t"+"%.2f" %(((seq.count("A")+seq.count("T"))/len(seq))*100)+"\t"\
+"%.2f" %(((seq.count("G")+seq.count("C"))/len(seq))*100)+"\t"+"\n")

# python base_composition.py <Fasta/Multi_fasta File>
