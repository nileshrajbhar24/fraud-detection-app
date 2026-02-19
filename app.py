import streamlit as st
import pandas as pd
import joblib

# 1. Load the Trained Model
model = joblib.load('fraud_model.pkl')

# 2. App Title and Description
st.title("🚨 Fraud Detection System")
st.write("Enter transaction details to check if it's **Legitimate** or **Fraudulent**.")

# 3. Sidebar for User Input
st.sidebar.header("Transaction Details")

# Define the input fields
type_options = ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN']
transaction_type = st.sidebar.selectbox("Transaction Type", type_options)

amount = st.sidebar.number_input("Amount ($)", min_value=0.0, value=1000.0)

st.sidebar.subheader("Sender Info")
oldbalanceOrg = st.sidebar.number_input("Old Balance (Sender)", min_value=0.0, value=5000.0)
newbalanceOrig = st.sidebar.number_input("New Balance (Sender)", min_value=0.0, value=4000.0)

st.sidebar.subheader("Recipient Info")
oldbalanceDest = st.sidebar.number_input("Old Balance (Recipient)", min_value=0.0, value=0.0)
newbalanceDest = st.sidebar.number_input("New Balance (Recipient)", min_value=0.0, value=0.0)

# 4. Create a DataFrame from the inputs
input_data = pd.DataFrame({
    'type': [transaction_type],
    'amount': [amount],
    'oldbalanceOrg': [oldbalanceOrg],
    'newbalanceOrig': [newbalanceOrig],
    'oldbalanceDest': [oldbalanceDest],
    'newbalanceDest': [newbalanceDest]
})

# 5. Display the Input Data
st.subheader("Transaction Summary")
st.write(input_data)

# 6. Predict Button
if st.button("Check for Fraud"):
    # Make Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # Display Result
    if prediction == 1:
        st.error(f"⚠️ FRAUD DETECTED! (Risk Probability: {probability:.2%})")
        st.write("This transaction looks suspicious. Please verify immediately.")
    else:
        st.success(f"✅ Legitimate Transaction (Risk Probability: {probability:.2%})")

        st.write("This transaction appears safe.")
