#!/usr/bin/python
#!python

# Importing Modules
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Loading Dataset
breast_cancer = load_breast_cancer()

# Converting to data.frame
df = pd.DataFrame(breast_cancer.data, columns = breast_cancer.feature_names)
df['diagnosis'] = breast_cancer.target

# Get the features and label from the original dataframe
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

# Performing standardization
sc = StandardScaler()
X_scaled = sc.fit_transform(X)

# Converting features to PCs
pca = PCA(n_components=3, whiten=True)
X_pca = pca.fit_transform(X_scaled)
df1 = pd.DataFrame(data = X_pca, columns = ["PC-1", "PC-2", "PC-3"])

# Subsets PCA data.frame into testing and training dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=True)

# Classifier
clf = MLPClassifier(random_state=1, max_iter=1000)

# Training
clf.fit(X_train, y_train)

# Testing
pred_val = clf.predict(X_test)

# Output
output = pd.DataFrame()
output['Expected Output'] = y_test
output['Predicted Output'] = pred_val

# Confusion Matrix
cmat = confusion_matrix(y_test, pred_val, labels=clf.classes_, normalize="true")
disp_cmat = ConfusionMatrixDisplay(confusion_matrix=cmat, display_labels=clf.classes_)

# Plotting Confusion Matrix
disp_cmat.plot(xticks_rotation='vertical')
plt.savefig('cmat.png',bbox_inches ="tight", pad_inches = 0.5)

# Usage: python brca_classifier-1.py
