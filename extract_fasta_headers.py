import sys
f_fasta = sys.argv[1]
mlti_fasta = open(f_fasta, "r")
head = open("fasta_headers.txt", "w")
for line in mlti_fasta:
	if line[0] == ">":
		head.write(line[1:])
head.close()
