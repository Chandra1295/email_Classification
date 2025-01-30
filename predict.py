import pickle
import pandas as pd
import numpy as np
from email_classifier.preprocess import handle_outliers  # Ensure consistency with training

# Load the trained model
with open("saved_models/email_classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Load the pre-trained encoders and scaler
with open("saved_models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("saved_models/onehot_encoder.pkl", "rb") as f:
    onehot_encoders = pickle.load(f)

# New input data (before encoding)
new_data = pd.DataFrame([
    {
        "subject_len": 59,
        "body_len": 12801,
        "mean_paragraph_len": 16,
        "category": 2,
        "product": 11,
        "no_of_CTA": 3,
        "mean_CTA_len": 23,
        "is_image": 1,
        "is_quote": 1,
        "is_weekend": 1,  # Raw categorical data
        "day_of_week": 5,
        "times_of_day": "Noon",
    }
])

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
print("Predicted Click Outcome:", predictions[0])

