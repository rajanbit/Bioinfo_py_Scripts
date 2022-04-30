import sys
file1 = sys.argv[1]
Dna = open(file1)
dna = Dna.readlines()
seq = ""
for line in dna:
	if line[0] != ">":
		seq = seq + line
no_a = seq.count("A")
no_t = seq.count("T")
no_g = seq.count("G")
no_c = seq.count("C")
dna_len = no_a + no_t + no_g + no_c
gc_percent = ((no_g + no_c)/dna_len)*100.0
print("GC content: " "%.2f" % gc_percent+"%")

# python gc_percent.py <FASTA_File>
