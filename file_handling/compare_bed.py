#!/usr/bin/python
#!python


# Compare two bed files for sequence overlaps

import sys

BED2 = open(sys.argv[2], "r")
BED1 = open(sys.argv[1], "r")
BED2_rl = BED2.readlines()
BED1_rl = BED1.readlines()
print("\n# Overlapping Regions . . . . . . . . . . . . . . . .\n")
for line2 in BED2_rl:
	BED2_tl= list(range(int(line2.split("\t")[1]),int(line2.split("\t")[2])))
	for line1 in BED1_rl:
		BED1_tl= list(range(int(line1.split("\t")[1]),int(line1.split("\t")[2])))
		
		out = any(check in BED1_tl for check in BED2_tl)
  
		if out:
			print("BED2:"+line2+"--BED1:"+line1)

# $ python compare_bed.py file1.bed file2.bed
