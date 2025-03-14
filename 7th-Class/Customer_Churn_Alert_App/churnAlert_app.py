import streamlit as st
import pickle
import pandas as pd
import numpy as np

def load_model():
    with open("7th-Class/Customer_Churn_Alert_App/churn_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def preprocess_input(user_input):
    # Convert user input dictionary to DataFrame
    input_df = pd.DataFrame([user_input])

    # Define categorical columns
    categorical_columns = [
        'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'
    ]

    # Apply one-hot encoding without removing numerical columns
    input_df = pd.get_dummies(input_df, columns=categorical_columns, drop_first=True)

    # Ensure all expected columns are present
    missing_cols = set(feature_names) - set(input_df.columns)
    for col in missing_cols:
        input_df[col] = 0  # Add missing columns with default value 0

    # Reorder columns to match training data
    input_df = input_df[feature_names]

    return input_df


def load_feature_names():
    with open("7th-Class/Customer_Churn_Alert_App/churn_feature_names.pkl", "rb") as file:
        feature_names = pickle.load(file)
    return feature_names


# Load model
model = load_model()
feature_names = load_feature_names()

# Streamlit App
st.title("Customer Churn Alert System")
st.write("Enter customer details to check the churn risk.")

# User Inputs
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, step=1)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=500.0, step=0.1)
total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, step=0.1)

gender = st.selectbox("Gender", ["Male", "Female"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["No", "Yes"])
online_backup = st.selectbox("Online Backup", ["No", "Yes"])
device_protection = st.selectbox("Device Protection", ["No", "Yes"])
tech_support = st.selectbox("Tech Support", ["No", "Yes"])
streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"])
streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

if st.button("Check Churn Risk"):
    user_data = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "gender": gender,
        "Partner": partner,
        "Dependents": dependents,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method
    }
    
    input_data = preprocess_input(user_data)
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ High Risk: The customer is likely to churn!")
    else:
        st.success("✅ Low Risk: The customer is unlikely to churn.")
