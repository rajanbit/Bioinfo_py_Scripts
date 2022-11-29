#!/usr/bin/python
#!python

# Importing Modules
import sys
from Bio import SeqIO
from random import randrange

# Function for FASTA to FASTQ conversion
def fastq_convertor(seq, header, frame):
	for i in range(frame,len(seq),int(sys.argv[4])):
		temphead = "@"+header+"_"+str(i)+"-"+str(i+int(sys.argv[4]))
		tempseq = seq[i:i+int(sys.argv[4])]
		qscore=""
		for j in range(1, 101):
			qscore+=score[randrange(36,42)]
		for k in range(101, 141):
			qscore+=score[randrange(31,36)]
		for l in range(141, 148):
			qscore+=score[randrange(20,31)]
		for m in range(148, len(tempseq)+1):
			qscore+=score[randrange(0,20)]
		fastq_out.write(temphead+"\n"+tempseq+"\n+\n"+qscore+"\n")

score="""!"#$&'()*+,-./0123456789:;<>=?@ABCDEFGHIJK"""

# Running everything ...
fasta_in = open(sys.argv[2])
fastq_out = open(sys.argv[8], "w+")
fasta_rec = SeqIO.parse(fasta_in, "fasta")
for rec in fasta_rec:
	seq, header = str(rec.seq), rec.id
	for x in range(1,int(sys.argv[6])+1):
		fastq_convertor(seq, header, x)

fasta_in.close()
fastq_out.close()

#Usage: $ python fasta2fastq.py -f <sequence.fasta> -l <read_length> -x <coverage> -o <sequence.fastq>
