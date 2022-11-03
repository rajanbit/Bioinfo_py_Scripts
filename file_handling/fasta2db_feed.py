# Importing modules
import sys
from Bio import SeqIO
import mysql.connector as mc
import hashlib

## Connecting to database
mysql=mc.connect( host="localhost", user="user1", passwd="", database="16srRNAdb")

## Feeding sequence data into database
fasta_rec = open(sys.argv[1])
data = SeqIO.parse(fasta_rec, "fasta")
for record in data:
	head, seq = record.id, str(record.seq)
	seq_hash = hashlib.md5(seq.encode())
	seq_md5 = seq_hash.hexdigest()
	mycursor=mysql.cursor()
	sql="insert into myseq(seqID, seq) values(%s, %s)"
	val=[(head, seq_md5)]
	mycursor.executemany(sql, val)
	mysql.commit()
	
## Usage: $ python fasta2db_feed.py <sequence.fasta>

