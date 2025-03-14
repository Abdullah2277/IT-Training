import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("salary_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit App
st.title("Salary Prediction App")
st.write("Enter your years of experience to predict your salary.")

# User Input
years_of_experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)

if st.button("Predict Salary"):
    # Reshape input as model expects a 2D array
    input_data = np.array([[years_of_experience]])
    predicted_salary = model.predict(input_data)[0]
    
    # Display prediction
    st.success(f"Predicted Salary: ${predicted_salary:,.2f}")
