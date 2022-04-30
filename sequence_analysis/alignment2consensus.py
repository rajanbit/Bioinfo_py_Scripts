### Import Modules
import sys
from Bio import AlignIO
from collections import Counter

### File Handling
out_file = open(sys.argv[1]+"_consen.fasta", "w")
conseq = ">consensus_"+sys.argv[1]+"\n"

### Read Alignment File
alignment = AlignIO.read(sys.argv[1], "fasta")

### Generate Consensus Sequence
for i in range (0, alignment.get_alignment_length()):
	temp_ls = []
	col_data = alignment[:,i]
	for data in Counter(col_data):
		if ((Counter(col_data)[data]/len(col_data))*100) >= 1 and data in ["A","T","G","C"]:
			temp_ls.append(data)
	if len(temp_ls) == 1 and ((Counter(col_data)[temp_ls[0]]/len(col_data))*100) >= 99:
		conseq += temp_ls[0]
	else:
		conseq += "-"

### Writing Output
out_file.write(conseq+"\n")
