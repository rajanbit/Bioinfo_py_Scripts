import random
nt_type = input("Enter the sequence type [RNA/DNA]: ")
nt_len = int(input("Enter the sequence length: "))
nt_DNA = "ATGC"
nt_RNA = "AUGC"
nt_seq = ""
x = ""
for i in range (int(nt_len)):
	x = random.randint(0, 3)
	if nt_type == "DNA":
		nt_seq = nt_seq + nt_DNA[x]
	if nt_type == "RNA":
		nt_seq = nt_seq + nt_RNA[x]
fasta_seq = ""
for i in range(0, len(nt_seq), 70):
	fasta_seq += nt_seq[i:i+70]+"\n"
print("> "+nt_type+"_Sequence")
print(fasta_seq)

# python random_seq_generator.py
