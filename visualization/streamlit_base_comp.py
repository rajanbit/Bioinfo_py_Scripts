#!/usr/bin/python
#!python

# Importing modules
import streamlit as st
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Base_Comp")

# Title
st.title("Nucleotide Composition Analysis")

# Subheader
st.subheader("This tool take FASTA sequence as input and generate nucleotide composition table and plots.")

# File uploader
st.header("FASTA File Upload")
uploaded_file = st.file_uploader("Upload a file", type=["fasta"])

# Creating empty dataframe
df = pd.DataFrame(columns=["Accession_IDs","Length","A","T","G","C","GC(%)"])

# Generating base composition table
if uploaded_file is not None:
	
	# Reading fasta records and filling the dataframe
	stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
	data = SeqIO.parse(stringio, "fasta")
	for record in data:
		header, seq = record.id, record.seq
		nucl_dict = {"Accession_IDs":0,"Length":0,"A": 0,  "T": 0, "G": 0, "C": 0,"GC(%)":0,}
		for nt in nucl_dict:
			nucl_dict[nt] = str(round((str(seq).count(nt)/len(seq))*100, 2))
		nucl_dict["Accession_IDs"] = header		
		nucl_dict["GC(%)"] = gc_fraction(seq)*100
		nucl_dict["Length"] = len(str(seq))	
		df = pd.concat([df, pd.DataFrame([nucl_dict])],ignore_index=True)
	
	# Writing table in app
	df.rename(columns = {"A":"A(%)", "T":"T(%)","G":"G(%)","C":"C(%)"}, inplace = True)
	st.text("Table 1. Nucleotide composition of given sequences.")
	st.write(df)

	# Plotting nucleotide base composition boxplot in app
	st.text("Figure 1. Boxplot showing nucleotide base composition of given sequences.")
	fig, ax = plt.subplots()
	new_df = df[["A(%)","T(%)","G(%)","C(%)"]].astype(float)	
	new_df.boxplot(column=["A(%)","T(%)","G(%)","C(%)"], grid=False)
	st.pyplot(fig)

	# Plotting GC composition boxplot in app
	st.text("Figure 2. Boxplot showing GC composition of given sequences.")
	fig, ax = plt.subplots()
	df.boxplot(column=["GC(%)"], grid=False)
	st.pyplot(fig)
	
	# Plotting length distribution boxplot in app
	st.text("Figure 3. Boxplot showing length distribution of given sequences.")
	fig, ax = plt.subplots()
	new_df = df[["Length"]].astype(float)
	new_df.boxplot(column=["Length"], grid=False)
	st.pyplot(fig)

## Usage: $ streamlit run streamlit_base_comp.py
