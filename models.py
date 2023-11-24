import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cardata.csv')

# choose relavent columns

df.columns

df_model = df[['Car_Name', 'Selling_Price', 'Miles_driven', 'Year']]
# get dummy data

df_dum = pd.get_dummies(df_model)
# train test split
from sklearn.model_selection import train_test_split 

x = df_dum.drop('Selling_Price', axis =1)
y = df_dum.Selling_Price.values
X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.33, random_state=42)
# multiple linear regressin
# Lasso Regression
# random Forest
# tune models Gridsearch CV
# test ensembles