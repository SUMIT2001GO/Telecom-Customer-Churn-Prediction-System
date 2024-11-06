# Telecom Customer Churn Prediction System

[Live Demo](https://telecom-customer-churn-prediction-system.streamlit.app/)

## Project Overview

The Telecom Customer Churn Prediction System is designed to predict whether a customer will churn (leave the service) based on various features like tenure, monthly charges, total charges, contract type, and more. This model is built to help telecom companies identify customers who are at risk of leaving, enabling targeted retention strategies and improving customer satisfaction.

## Model Overview

The model is developed using **Random Forest Classifier** and enhanced with **SMOTEENN** (Synthetic Minority Over-sampling Technique with Edited Nearest Neighbors) to handle class imbalance in the dataset. The use of SMOTEENN significantly improves model performance by resampling the minority class and making the decision boundaries more effective.

### Key Features:
- **Input Features**: Tenure, Monthly Charges, Total Charges, Contract Type, Dependents, and Partner status.
- **Model**: Random Forest Classifier.
- **SMOTEENN**: Used to address class imbalance in the data and improve prediction accuracy.

## Model Performance

### Without SMOTEENN:
- **Accuracy**: 81.59%
- **Precision (Churn)**: 0.72
- **Recall (Churn)**: 0.49
- **F1-Score**: 0.58
- ![Screenshot 2024-11-06 223850](https://github.com/user-attachments/assets/6a726b96-24ff-4f14-abe5-fec83eb2cedd)


### With SMOTEENN:
- **Accuracy**: 92.52%
- **Precision (Churn)**: 0.91
- **Recall (Churn)**: 0.96
- **F1-Score**: 0.93
- ![Screenshot 2024-11-06 223855](https://github.com/user-attachments/assets/a8b014d9-36f7-40d6-8261-8d1b3dd62e6a)


By applying **SMOTEENN**, the model's performance improved drastically, particularly in predicting the minority class (churn), leading to better recall and more accurate results.

## Business Objective

Customer churn prediction is crucial for telecom companies to:
1. Identify high-risk customers and proactively intervene to retain them.
2. Minimize customer attrition by offering personalized incentives and services.
3. Improve customer satisfaction and loyalty by addressing issues before they lead to churn.

## How the Model Works

- **Data Preprocessing**: The dataset is cleaned, and relevant features are selected for prediction. One-hot encoding is applied to categorical features such as Contract, Dependents, and Partner.
- • Removing Duplicate Records 
• Removing Unique Value Variables 
• Removing Zero Variance Variables 
• Outlier Treatment 
            Using Boxplot: Q3+(1.5IQR) & Q1-(1.5IQR) 
           Standardization: +/- 3 Sigma approach 
           Capping & Flooring 
• Removing the Highly Correlated Variables 
• Performed Multicollinearity (VIF > 5).

- **Model Training**: A Random Forest Classifier is trained on the processed data, first without any resampling techniques, and then with **SMOTEENN** to address class imbalance.
- **Prediction**: The trained model predicts the likelihood of churn based on input features. A higher probability indicates a higher likelihood that the customer will churn.
![Screenshot 2024-11-06 223902](https://github.com/user-attachments/assets/23f8436c-e20a-4986-825b-81e2b519ea3d)

## Future Objectives

- **Integration with Customer Databases**: In the future, the system can be integrated with a telecom company's customer database for real-time churn prediction.
- **Model Improvement**: The model can be further improved by incorporating additional features such as customer complaints, network issues, and more advanced machine learning techniques (e.g., XGBoost, LightGBM).
- **Deployment**: The system could be extended into a full-fledged service where telecom companies can input customer data directly and receive real-time predictions.

## How to Use the App

1. **Visit the Live Demo**: You can try the app live by visiting the [Streamlit app](https://telecom-customer-churn-prediction-system.streamlit.app/).
2. **Input Customer Data**: Enter customer details such as tenure, monthly charges, contract type, and whether they have dependents or a partner.
3. **Predict Churn**: Click the "Predict Churn" button to get a prediction of whether the customer is likely to churn or not.

## How to Run the Model Locally

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/SUMIT2001GO/Telecom-Customer-Churn-Prediction-System.git
    cd telecom-churn-prediction
    ```

2. **Install Dependencies**:
    You can install the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

4. **Input Data**: After the app starts, you can enter the required customer data and click on "Predict Churn" to get the prediction.

## Repository Structure

- `app.py`: The main file that runs the Streamlit app.
- `telecom1_churn.csv`: The dataset used for training the model.
- `churn_rf_model.pkl`: The trained Random Forest model.
- `requirements.txt`: List of dependencies required to run the app.


## Acknowledgements

- **SMOTEENN**: Used to balance the dataset and improve the performance of the Random Forest model.
- **Streamlit**: Used to create the interactive web application for predictions.

---

This README should provide clear instructions on how to use the project, explain its purpose, and give a detailed overview of the model's performance and business objectives.
