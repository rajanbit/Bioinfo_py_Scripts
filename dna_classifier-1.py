#!/usr/bin/python
#!python

# Importing Modules
import sys
import numpy as np
from sklearn.neural_network import MLPClassifier

# Input Data
training_data = (open(sys.argv[1], "r")).readlines()
test_data = (open(sys.argv[2], "r")).readlines()

# Sequence Encoder (one hot encoding)
def sequence_encoder(seq):
	seq_mat = []
	temp = ""
	for i in range(0, len(seq)):
		if seq[i].upper() == "A":
			temp+="1000"
		elif seq[i].upper() == "T":
			temp+="0100"
		elif seq[i].upper() == "G":
			temp+="0010"
		elif seq[i].upper() == "C":
			temp+="0001"
		else:
			temp+="0000"
	temp = list(temp)
	temp1 = [int(j) for j in temp]
	return(temp1)

# Feature Matrix Generator
def matrix_generator(data):
	
	feature_matrix = []
	seq = ""
	label = []
	for line in training_data:
		if line[0] == ">" and seq == "":
			label.append(line.strip().replace(">", ""))
		elif line[0]!= ">":
			seq += line.strip()
		elif line[0] == ">" and seq != "":
			feature_matrix.append(sequence_encoder(seq))
			seq=""
			label.append(line.strip().replace(">", ""))
	feature_matrix.append(sequence_encoder(seq))
	return(feature_matrix, label)


# Generate feature matrix for training dataset 
dataset = matrix_generator(training_data)

# Feature Matrix
X = np.array(dataset[0])
# Labels
y = np.array(dataset[1])

# Classifier
model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(4), max_iter=5000)

# Training
model.fit(X, y)

# Generate feature matrix for testing dataset 
dataset2 = matrix_generator(test_data)

# Prediction
print("label [Predicted]")
for data in [0,1]:
	print(dataset2[1][data],model.predict(np.array([dataset2[0][data]])))

# Usage: $ python dna_classifier-1.py <train.fasta> <test.fasta>
