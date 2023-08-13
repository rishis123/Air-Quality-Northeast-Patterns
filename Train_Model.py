import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import preprocessing
from sklearn.metrics import r2_score

# importing data
df = pd.read_excel('Data\CarbonMonoxideFile.xlsx')
df = df.dropna()

X = df.drop(['Gases', 'Unnamed: 0', 'Mean Value'], axis= 1)
y = df['Mean Value']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=101)

print(X)

model = LinearRegression()

model.fit(X_train,y_train)

predictions = model.predict(X_test)

r_squared = r2_score(predictions, y_test)

print(
  'mean_squared_error : ', mean_squared_error(y_test, predictions))
print(
  'mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print(r_squared)