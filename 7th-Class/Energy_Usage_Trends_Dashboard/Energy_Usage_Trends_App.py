import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report
import streamlit as st

df = pd.read_csv("7th-Class/Energy_Usage_Trends_Dashboard/owid-energy-data.csv")
# Display column names to check the correct column name for energy consumption
st.write("Dataset Columns:", df.columns.tolist())

# Identify the correct column for energy consumption
energy_columns = [col for col in df.columns if "consumption" in col.lower()]

if not energy_columns:
  raise KeyError("No column related to energy consumption found in the dataset.")

# Use the first identified energy consumption column
energy_column = energy_columns[0]
st.write(f"Using '{energy_column}' as the target variable.")

df.dropna(inplace=True)

categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

if categorical_cols:
  df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

X = df.drop(columns=[energy_column])
y = df[energy_column]

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state = 7)

model = LinearRegression()
model.fit(Xtrain,ytrain)

y_pred = model.predict(Xtest)

mse = mean_squared_error(ytest,y_pred)
r2 = r2_score(ytest,y_pred)


# Streamlit app
st.title('Energy Consumption Prediction')
st.write(f'MSE: {mse:.2f}, R-squared: {r2:.2f}')

# Visualization
fig, ax = plt.subplots()
ax.scatter(ytest, y_pred, alpha=0.5, color='blue')
ax.plot([ytest.min(), ytest.max()], [ytest.min(), ytest.max()], 'r',lw=2)
ax.set_xlabel('Actual Energy Consumption')
ax.set_ylabel('Predicted Energy Consumption')
st.pyplot(fig)

# User input for prediction
st.sidebar.header('Predict Energy Consumption')
features = {col: st.sidebar.number_input(f'Enter {col}:',
float(df[col].min()), float(df[col].max())) for col in X.columns}
if st.sidebar.button('Predict'):
    input_data = np.array([features[col] for col in X.columns]).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    st.sidebar.write(f'Predicted Energy Consumption: {prediction:.2f} kWh')
