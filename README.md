#  Financial Fraud Detection System

##  Project Overview

This project is an end-to-end Machine Learning solution designed to detect fraudulent financial transactions. Using a dataset of simulated mobile money transactions, the system identifies malicious behavior (such as account takeovers and money laundering) in real-time. The final product includes a trained **Random Forest Classifier** deployed as an interactive web application using **Streamlit**.

##  Dataset Details

The model is trained on a dataset containing financial transactions.

* **Target Variable:** `isFraud` (0 = Legitimate, 1 = Fraudulent)
* **Key Features Used:**
* `type`: The type of transaction (e.g., PAYMENT, TRANSFER, CASH_OUT).
* `amount`: The total amount of the transaction.
* `oldbalanceOrg`: Initial balance of the sender before the transaction.
* `newbalanceOrig`: New balance of the sender after the transaction.
* `oldbalanceDest`: Initial balance of the recipient before the transaction.
* `newbalanceDest`: New balance of the recipient after the transaction.



###  Key Data Insights

During the Exploratory Data Analysis (EDA) phase, several critical patterns were discovered:

1. **Transaction Types:** 100% of the fraudulent transactions occurred exclusively in `TRANSFER` and `CASH_OUT` transaction types.
2. **The "Account Emptying" Pattern:** Fraudsters consistently transferred the exact amount of the sender's total balance (`amount == oldbalanceOrg`), draining the account to zero.
3. **Mule Accounts:** Fraudulent transfers frequently targeted destination accounts with an initial balance of exactly zero.

##  Machine Learning Model

* **Algorithm:** Random Forest Classifier
* **Preprocessing:** * `OneHotEncoder` was used to convert categorical transaction types into numerical features.
* A `scikit-learn Pipeline` was utilized to bundle preprocessing and modeling, preventing data leakage and ensuring seamless deployment.


* **Performance:** * **Accuracy:** ~99.7%
* **Recall (Fraud Detection Rate):** ~95%
* The model is highly precise, minimizing false alarms while successfully catching the vast majority of fraudulent behavior.



##  Tech Stack

* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn
* **Data Visualization:** Matplotlib, Seaborn
* **Web Deployment:** Streamlit
* **Model Serialization:** Joblib

##  How to Run the App Locally

Follow these steps to run the Fraud Detection web application on your local machine.

**1. Clone the repository:**

```bash
git clone https://github.com/nileshrajbhar24/fraud-detection-app.git
cd fraud-detection-app

```

**2. Install the required dependencies:**

```bash
pip install -r requirements.txt

```

**3. Run the Streamlit web app:**

```bash
streamlit run app.py

```

## Live Demo

**App Link**: https://nileshrajbhar24-fraud-detection-app.streamlit.app/

## Project Structure

```text
├── app.py                      # Main Streamlit application code
├── train_and_save_model.py     # Script to build, train, and save the ML pipeline
├── fraud_model.pkl             # Serialized Machine Learning model (Pipeline)
├── requirements.txt            # Python dependencies
├── Fraud_Analysis_Dataset.csv  # Dataset used for training (Add to .gitignore if large)
└── README.md                   # Project documentation

```

## Testing the Model

To test the model's accuracy in the app, try these two scenarios:

* **Fraud Trigger:** Select `TRANSFER`, set Amount to `50000`, Sender Old Balance to `50000`, Sender New Balance to `0`, and Recipient Old Balance to `0`. (The app will flag this as Fraud).
* **Safe Transaction:** Select `PAYMENT` or `CASH_IN` with any normal numbers. (The app will flag this as Legitimate).

---

**Author:** Nilesh Rajbhar

**Date:** February 2026
