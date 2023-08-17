import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score
from sklearn import preprocessing
from sklearn.metrics import r2_score

# importing data
df = pd.read_excel('Data/CarbonMonoxideFile.xlsx')
df = df.dropna()
df['Mean Value'] = pd.to_numeric(df['Mean Value'], errors='coerce')

# Calculate IQR for the "Mean Value" column
Q1 = df['Mean Value'].quantile(0.25)
Q3 = df['Mean Value'].quantile(0.75)
IQR = Q3 - Q1

# Filter outliers from the "Mean Value" column
# df = df[~((df['Mean Value'] < (Q1 - 1.5 * IQR)) | (df['Mean Value'] > (Q3 + 1.5 * IQR)))]

X = df.drop(['Gases', 'Unnamed: 0', 'Mean Value'], axis=1)
y = df['Mean Value']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)

model = RandomForestRegressor()

model.fit(X_train, y_train)  # Train model on training data (80% of dataset)

# Run model on testing data (20% of dataset)
predictions = model.predict(X_test)

r_squared = r2_score(y_test, predictions)

print('mean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print(r_squared)
