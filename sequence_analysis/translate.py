#!/usr/bin/python
#!python

import sys

f_file = sys.argv[1]
f_open = open(f_file, "r")
f_read = f_open.readlines()

codon_table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*', 
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'} 

head = ""
seq = ""
rev_seq = ""
for line in f_read:
	if ">" in line[0:2]:
		head = line
	elif ">" not in line[0:2]:
		seq += line.strip()
for i in reversed(range(0, len(seq))):
	if seq[i] == "A":
		rev_seq = rev_seq + "T"
	elif seq[i] == "T":
		rev_seq = rev_seq + "A"
	elif seq[i] == "G":
		rev_seq = rev_seq + "C"
	elif seq[i] == "C":
		rev_seq = rev_seq + "G"

# FRAME I Forward
prot_seq_IF = ""
for x in range(0,len(seq),3):
	codon = seq[x:x+3]
	if len(codon) == 3:
		aa = codon_table.get(codon)
		prot_seq_IF += aa
# FRAME II Forward
prot_seq_IIF = ""
for x in range(1,len(seq),3):
	codon = seq[x:x+3]
	if len(codon) == 3: 
		aa = codon_table.get(codon)
		prot_seq_IIF += aa
# FRAME III Forward
prot_seq_IIIF = ""
for x in range(2,len(seq),3):
	codon = seq[x:x+3]
	if len(codon) == 3: 
		aa = codon_table.get(codon)
		prot_seq_IIIF += aa
# FRAME I Reverse
prot_seq_IR = ""
for x in range(0,len(rev_seq),3):
	codon = rev_seq[x:x+3]
	if len(codon) == 3:
		aa = codon_table.get(codon)
		prot_seq_IR += aa
# FRAME II Reverse
prot_seq_IIR = ""
for x in range(1,len(rev_seq),3):
	codon = rev_seq[x:x+3]
	if len(codon) == 3:
		aa = codon_table.get(codon)
		prot_seq_IIR += aa
# FRAME III Reverse
prot_seq_IIIR = ""
for x in range(2,len(rev_seq),3):
	codon = rev_seq[x:x+3]
	if len(codon) == 3:
		aa = codon_table.get(codon)
		prot_seq_IIIR += aa

def out(prot_seq):
	prot_fasta = ""
	for i in range(0, len(prot_seq), 70):
		prot_fasta += prot_seq[i:i+70]+"\n"
	print(prot_fasta)

print(">5'3' Frame I")
out(prot_seq_IF)
print(">5'3' Frame II")
out(prot_seq_IIF)
print(">5'3' Frame III")
out(prot_seq_IIIF)
print(">3'5' Frame I")
out(prot_seq_IR)
print(">3'5' Frame II")
out(prot_seq_IIR)
print(">3'5' Frame III")
out(prot_seq_IIIR)

# Usage: python translate.py file.fasta
