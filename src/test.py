from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Ridge
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('../data/Medical_insurance.csv')
#  Clean the data by handling missing values
df.dropna(inplace=True)

#  Exploratory Data Analysis (EDA)
#  Correlation matrix to identify attributes that most affect the charges
corr_matrix = df.corr()
print(corr_matrix['charges'].sort_values(ascending=False))

#  Visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

#  Single variable Linear Regression model

 # Using 'bmi' as the single variable
X = df[['bmi']]
y = df['charges']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_pred = lin_reg.predict(X_test)

print(f'Single Variable Linear Regression - MSE: {mean_squared_error(y_test, y_pred)}, R2: {r2_score(y_test, y_pred)}')

 # Multi-variable Linear Regression model
X = df[['age', 'bmi', 'children', 'smoker', 'region']]
X = pd.get_dummies(X, drop_first=True)  #  Convert categorical variables to dummy variables
y = df['charges']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_pred = lin_reg.predict(X_test)

print(f'Multi-variable Linear Regression - MSE: {mean_squared_error(y_test, y_pred)}, R2: {r2_score(y_test, y_pred)}')

#  Ridge Regression model

ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(X_train, y_train)

y_pred = ridge_reg.predict(X_test)

print(f'Ridge Regression - MSE: {mean_squared_error(y_test, y_pred)}, R2: {r2_score(y_test, y_pred)}')