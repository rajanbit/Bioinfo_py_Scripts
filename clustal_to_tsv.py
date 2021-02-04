import sys
import re

msa_open = open(sys.argv[1], "r")
msa_rl = msa_open.readlines()
tsv = open("result.tsv", "w+")

s_char = ["*",":",]

temp = ""
for line in msa_rl:
	line = line.strip()

	if "CLUSTAL" in line:
		temp+=line+"\n"
		
	elif line == "":
		temp += "\n"

	elif line == "\n":
		temp += "\n"

	else:
		m = re.search(r'\d+$', line)

		if m is not None:
			line = line.replace("\t", ",")
			line = re.sub("\s\s+", ",",line).split(",")
			temp += line[0]+"\t"
			for i in range(0,len(line[1])):
				temp += line[1][i]+"\t"
			temp += line[2]+"\n"
tsv.write(temp)
