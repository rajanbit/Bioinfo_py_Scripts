''' \
Usage:
   python dna_fasta_visualization.py -n <FASTA_File> '''

import sys
import re

...

class text():
	red = '\033[31m'
	green = '\033[32m'
	yellow = '\033[33m'
	blue = '\033[34m'
	purple='\033[35m'
	default = '\033[0m'
	black = "\x1b[30m"
	cyan = '\033[36m'
	bg = "\x1b[107m"

inputs = sys.argv
if '-n' not in inputs:
	print (__doc__)
else:
	in_file = inputs[inputs.index('-n') + 1]
	file1 = open(in_file)
	seq_data = file1.readlines()
	header = ""
	seq = ""
	for line in seq_data:
		if line.startswith(">"):
			header += line.strip()
		else:
			seq += line

	f_seq1 = seq.replace("A",(text.red+"A"+text.default))
	f_seq2 = f_seq1.replace("T",(text.blue+"T"+text.default))
	f_seq3 = f_seq2.replace("G",(text.green+"G"+text.default))
	f_seq4 = f_seq3.replace("C",(text.yellow+"C"+text.default))
	
	print("\n"+text.bg+text.black+header+text.default)
	if len(seq) <= 10000:
		print(f_seq4+"\n")
	else:
		print(text.red+"\n     #######################################################\n\
     ## DNA sequence is extremely long for visualization! ##\n\
     #######################################################"+text.default)

	no_A = seq.count("A")
	no_T = seq.count("T")
	no_G = seq.count("G")
	no_C = seq.count("C")
	
	acc_regex= re.compile(r'\S\S_\d\d\d\d\d\d.\d')
	acc_id = acc_regex.search(header)
	
	print("\n"+text.bg+text.black+"Sequence Information:"+text.default+"\n")

	print("Accession number: " + text.cyan+acc_id.group()+text.default+"\n")

	list_head = header.split()
	start_ind = 1
	if "complete" in list_head:
		end_ind = list_head.index("complete")
		print("Organism/Origin: "+text.cyan+(" ".join(list_head[start_ind:end_ind]).replace(",",""))+text.default+"\n")

	print("Number of Adenine residues" +text.red+" [A]"+text.default+": "+str(no_A))
	print("Number of Guanine residues" +text.green+" [G]"+text.default+": "+str(no_G))
	print("Number of Cytosine residues" +text.yellow+" [C]"+text.default+": "+str(no_C))
	print("Number of Thymine residues" +text.blue+" [T]"+text.default+": "+str(no_T)+"\n")

	print("DNA Sequence length" +text.purple+" [l]"+text.default+": "+str(len(seq))+"\n")

	gc_per = ((no_G + no_C)/len(seq))*100.0
	at_per = ((no_A + no_T)/len(seq))*100.0

	print("GC content"+text.green+" [G"+text.default+text.yellow+"C]"+text.default+": "+"%.2f" % gc_per+"%")
	print("AT content"+text.red+" [A"+text.default+text.blue+"T]"+text.default+": "+"%.2f" % at_per+"%"+"\n")

	if gc_per >= 60:
		print("The DNA is"+text.green+" [G"+text.default+text.yellow+"C] "+text.default+"rich"+"\n")
	elif at_per >= 60:
		print("The DNA is"+text.red+" [A"+text.default+text.blue+"T] "+text.default+"rich"+"\n")
...

