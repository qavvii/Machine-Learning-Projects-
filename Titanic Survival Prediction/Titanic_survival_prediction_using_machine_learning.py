# -*- coding: utf-8 -*-
"""Project 15. Titanic Survival Prediction using Machine Learning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10ew-X3b9wgMQSPymh-4z0Kn8qjYEg92N

Importing the Dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection & Processing"""

# load the data from csv file to Pandas DataFrame
titanic_data = pd.read_csv('/content/train.csv')

# printing the first 5 rows of the dataframe
titanic_data.head()

# number of rows and Columns
titanic_data.shape

# getting some informations about the data
titanic_data.info()

# check the number of missing values in each column
titanic_data.isnull().sum()

"""Handling the Missing values"""

# drop the "Cabin" column from the dataframe
titanic_data = titanic_data.drop(columns='Cabin', axis=1)

# replacing the missing values in "Age" column with mean value
titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)

# finding the mode value of "Embarked" column
print(titanic_data['Embarked'].mode())

print(titanic_data['Embarked'].mode()[0])

# replacing the missing values in "Embarked" column with mode value
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)

# check the number of missing values in each column
titanic_data.isnull().sum()

"""Data Analysis"""

# getting some statistical measures about the data
titanic_data.describe()

# finding the number of people survived and not survived
titanic_data['Survived'].value_counts()

"""Data Visualization"""

sns.set()

# making a count plot for "Survived" column
sns.countplot('Survived', data=titanic_data)

titanic_data['Sex'].value_counts()

# making a count plot for "Sex" column
sns.countplot('Sex', data=titanic_data)

# number of survivors Gender wise
sns.countplot('Sex', hue='Survived', data=titanic_data)

# making a count plot for "Pclass" column
sns.countplot('Pclass', data=titanic_data)

sns.countplot('Pclass', hue='Survived', data=titanic_data)

"""Encoding the Categorical Columns"""

titanic_data['Sex'].value_counts()

titanic_data['Embarked'].value_counts()

# converting categorical Columns

titanic_data.replace({'Sex':{'male':0,'female':1}, 'Embarked':{'S':0,'C':1,'Q':2}}, inplace=True)

titanic_data.head()

"""Separating features & Target"""

X = titanic_data.drop(columns = ['PassengerId','Name','Ticket','Survived'],axis=1)
Y = titanic_data['Survived']

print(X)

print(Y)

"""Splitting the data into training data & Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training

Logistic Regression
"""

model = LogisticRegression()

# training the Logistic Regression model with training data
model.fit(X_train, Y_train)

"""Model Evaluation

Accuracy Score
"""

# accuracy on training data
X_train_prediction = model.predict(X_train)

print(X_train_prediction)

training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
print('Accuracy score of training data : ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)

print(X_test_prediction)

test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
print('Accuracy score of test data : ', test_data_accuracy)

