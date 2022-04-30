import sys
f_file = sys.argv[1]
mlti_fasta = open(f_file, "r")
acc_no = open("accession_no.txt", "w+")
for line in mlti_fasta:
	if line[0] == ">":
		acc_no.write(line[1:10] + "\n")

# python extract_accession_no.py <Multi_FASTA_File>
