import sys
DNA_file = sys.argv[1]
k_mer_size = input("Enter the K-mer length: ")
DNA = open(DNA_file, "r")
seq = ""
for line in DNA:
	if line.startswith(">"):
		pass
	else:
		seq += line.replace('\n', "")
x = int(k_mer_size)
for i in range(len(seq) - x):
	print(seq[i:i+int(k_mer_size)])

# python k-mer_constructor.py <FASTA_File>
