# -*- coding: utf-8 -*-
"""Diabetes Prediction .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ASNamVFcxAlYeYQcyIfdJ-NdCo_7_j0e
"""

# prompt: import /content/diabetes.csv this

import pandas as pd

df = pd.read_csv('/content/diabetes.csv')
print(df.head()) # Print the first few rows to check if it loaded correctly

# prompt: import numpy  pandas standardscaler traintestsplit svm accuracy_score

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score
diabetes_dataset = pd.read_csv('/content/diabetes.csv')



# printing the first 5 rows of the dataset
diabetes_dataset.head()

# number of rows and Columns in this dataset
diabetes_dataset.shape

# getting the statistical measures of the data
diabetes_dataset.describe()

# prompt: value count of outcome then groupby  outcome .mean()

# Assuming 'Outcome' is the column you want to analyze
outcome_counts = df['Outcome'].value_counts()
print(outcome_counts)

"""o means non diabetes



1 means diabetes
"""

# Group by 'Outcome' and calculate the mean of other columns
mean_by_outcome = df.groupby('Outcome').mean()
mean_by_outcome

# separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']

print(X)

print(Y)

# Feature scaling using StandardScaler
scaler = StandardScaler()


scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X)
print(Y)

# prompt: fit and transform  using standardscaler

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

from sklearn import svm

classifier = svm.SVC(kernel='linear')

#training the support vector Machine Classifier
classifier.fit(X_train, Y_train)

# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of the training data : ', training_data_accuracy)

# accuracy score on the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data : ', test_data_accuracy)

import numpy as np

input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')







