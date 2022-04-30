''' \
Usage:
   python file_comparison.py -f1 <File_1> -f2 <File_2>'''

import sys
...

inputs = sys.argv
if '-f1' not in inputs  or '-f2' not in inputs:
	print (__doc__)
else:
	file1 = inputs[inputs.index('-f1') + 1]
	file2 = inputs[inputs.index('-f2') + 1]
	db = open(file1, "r")
	qr = open(file2, "r")
	db_list = []
	qr_list = []
	for line in db:
		db_list.append(line)
	for line in qr:
		qr_list.append(line)
	print("Data not in f2:")
	for data1 in db_list:
		if data1 not in qr_list:
			f1_data = data1
			print(f1_data)
	print("Data not in f1:")
	for data2 in qr_list:
		if data2 not in db_list:
			f2_data = data2
			print(f2_data)
...

# python file_comparison.py -f1 <File_1> -f2 <File_2>
