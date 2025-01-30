Email Click Prediction using Machine Learning

📌 Project Overview

This project aims to predict whether an email will be clicked based on various features such as email length, number of call-to-actions (CTAs), subject line length, and time of day. The classification is performed using machine learning models trained on historical email marketing data.

📊 Data Analysis & Preprocessing

Two Jupyter notebooks were used for data analysis and machine learning model development:

Exploratory Data Analysis (EDA) & Preprocessing:

Performed data cleaning and handled missing values.

Conducted feature engineering (e.g., extracting day of the week, categorizing times of day).

Applied outlier handling for numerical features.

Encoded categorical variables using One-Hot Encoding.

Model Training & Evaluation:

Trained multiple machine learning models including Logistic Regression, Random Forest, and XGBoost.

Tuned hyperparameters to optimize performance.

Evaluated models using accuracy, precision, recall, and F1-score.

Selected the best model for deployment.

🚀 Web Application

A Flask-based web application is developed to classify new email data.

How it Works:

The user sends email feature data via a POST request.

The app processes the data (applies encoding, scaling, and outlier handling).

The trained model predicts whether the email will be clicked or not.

The result is displayed in the UI.

Installation & Setup

# Clone the repository
git clone https://github.com/your-repo/email-click-classifier.git
cd email-click-classifier

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

API Endpoints

1. Home Page

URL: /

Method: GET

Response: Renders the index.html page.

2. Predict Clickability

URL: /predict

Method: POST

Request Body: JSON containing email features.

Response: JSON with prediction result (Clicked or Not Clicked).

Example request:

{
    "no_of_CTA": 2,
    "mean_paragraph_len": 50,
    "body_len": 500,
    "subject_len": 30,
    "mean_CTA_len": 15,
    "is_weekend": 0,
    "day_of_week": "Monday",
    "times_of_day": "Morning"
}

📌 Future Enhancements

Implement deep learning models for improved accuracy.

Deploy the app as a cloud-based API.

Integrate real-time email campaign data for live predictions.

📢 Contributions are welcome! Feel free to submit a PR or raise an issue.

