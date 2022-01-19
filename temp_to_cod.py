#!/usr/bin/python
#!python

temp_strand = input("Enter the DNA Sequence: ")

cod_strand = ""

for i in range(0, len(temp_strand)):

	if temp_strand[i] == "A":
		cod_strand = cod_strand + "T"
	elif temp_strand[i] == "T":
		cod_strand = cod_strand + "A"
	elif temp_strand[i] == "G":
		cod_strand = cod_strand + "C"
	elif temp_strand[i] == "C":
		cod_strand = cod_strand + "G"

print(cod_strand) 
