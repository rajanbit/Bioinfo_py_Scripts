#!/usr/bin/python
#!python

# Importing Modules
import sys
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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
	for line in data:
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
dataset1 = matrix_generator(training_data)
#print(dataset1)
# Feature matrix for training
X_train = np.array(dataset1[0])

# Labels for training
y_train = np.array(dataset1[1])

# Classifier
model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(4), max_iter=5000)

# Training
model = model.fit(X_train, y_train)

# Generate feature matrix for testing dataset
dataset2 = matrix_generator(test_data)

# Feature matrix for testing
X_test = np.array(dataset2[0])

# Labels for testing
y_test = np.array(dataset2[1])

# Prediction
y_predict = model.predict(X_test)

# Plotting Confusion Matrix
cmat = confusion_matrix(y_test, y_predict, labels=model.classes_)
disp_cmat = ConfusionMatrixDisplay(confusion_matrix=cmat, display_labels=model.classes_)
disp_cmat.plot(xticks_rotation='vertical')
plt.savefig('cmat.png',bbox_inches ="tight", pad_inches = 0.5)

# Usage: $ python dna_classifier-1.py <train.fasta> <test.fasta>
