#!/usr/bin/python
#!python

# Importing Modules
import sys
from Bio import SeqIO

# Function for FASTQ to FASTA conversion
fastq_in = open(sys.argv[1])
fasta_out = open(sys.argv[1]+".fasta", "w+")
fastq_rec = SeqIO.parse(fastq_in, "fastq")
for rec in fastq_rec:
    fasta_out.write(">"+rec.id+"\n"+str(rec.seq)+"\n")

fastq_in.close()
fasta_out.close()

# Usage: python fastq2fasta.py <seq.fastq>

