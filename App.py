import streamlit as st
import pandas as pd
import joblib

# Load the saved model and a sample of the original training data
model = joblib.load('churn_rf_model.pkl')
original_data = pd.read_csv('telecom1_churn.csv')
original_data = original_data.drop(['Unnamed: 0', 'Churn'], axis=1)

def predict_churn(input_data):
    input_data_aligned = pd.DataFrame(input_data, columns=original_data.columns).reindex(columns=original_data.columns, fill_value=0)
    prediction = model.predict(input_data_aligned)
    return "Churn" if prediction[0] == 1 else "No Churn"

st.title("Telecom Churn Prediction System")
st.write("Enter Customer Details Below To Predict Churn.")

tenure = st.number_input("Tenure (months)", min_value=0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
partner = st.selectbox("Partner", ["Yes", "No"])

user_input = {
    'tenure': tenure,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    f'Contract_{contract}': 1,
    f'Dependents_{dependents}': 1,
    f'Partner_{partner}': 1,
}

user_data = pd.DataFrame([user_input]).reindex(columns=original_data.columns, fill_value=0)
if st.button("Predict Churn"):
    result = predict_churn(user_data)
    st.write(f"The prediction is: **{result}**")
