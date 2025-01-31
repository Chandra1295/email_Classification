import pickle
import pandas as pd
import numpy as np
import os
from flask import Flask, render_template, request, jsonify
from email_classifier.preprocess import handle_outliers  # Ensure consistency with training

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open("saved_models/email_classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Load the pre-trained encoders and scaler
with open("saved_models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("saved_models/onehot_encoder.pkl", "rb") as f:
    onehot_encoders = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    new_data = pd.DataFrame([request.json])

    # Apply outlier handling (same as in preprocess.py)
    outlier_features = ['no_of_CTA', 'mean_paragraph_len', 'body_len', 'subject_len', 'mean_CTA_len']
    for feature in outlier_features:
        if feature in new_data.columns:
            new_data[feature] = handle_outliers(new_data, feature)

    # Apply one-hot encoding using saved encoders
    onehot_features = ['is_weekend', 'day_of_week', 'times_of_day']
    for feature in onehot_features:
        if feature in new_data.columns:
            encoder = onehot_encoders[feature]
            encoded_values = encoder.transform(new_data[[feature]])
            encoded_df = pd.DataFrame(encoded_values, 
                                      columns=encoder.get_feature_names_out([feature]), 
                                      index=new_data.index)
            new_data = new_data.drop(columns=[feature]).join(encoded_df)
        else:
            print(f"Warning: {feature} missing in new data, using zeros as placeholders.")
            encoded_df = pd.DataFrame(np.zeros((new_data.shape[0], len(encoder.get_feature_names_out([feature])))),
                                      columns=encoder.get_feature_names_out([feature]), 
                                      index=new_data.index)
            new_data = new_data.join(encoded_df)

    # Ensure feature alignment (to match model training)
    expected_features = scaler.feature_names_in_
    new_data = new_data.reindex(columns=expected_features, fill_value=0)

    # Standardization
    new_data_scaled = scaler.transform(new_data)

    # Make predictions
    predictions = model.predict(new_data_scaled)
    prediction_result = "Clicked" if predictions[0] == 1 else "Not Clicked"

    # Return JSON response with prediction result
    #return jsonify({'prediction': prediction_result})
    return render_template('result.html', prediction=prediction_result)

DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=DEBUG_MODE)
