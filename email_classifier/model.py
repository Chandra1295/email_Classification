import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from preprocess import preprocess_data
import os

import warnings

# Ignore specific warnings
warnings.filterwarnings("ignore", category=FutureWarning, message=".*sparse.*")

# Load training dataset
df_train = pd.read_csv("/home/csc/Documents/GitHub/email_Classification/data/train.csv")

# Preprocess data
X_train, X_valid, y_train, y_valid, scaler, onehot_encoders = preprocess_data(df_train)

# Save the fitted StandardScaler

os.makedirs("saved_models", exist_ok=True)

with open("saved_models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Save OneHotEncoders
with open("saved_models/onehot_encoder.pkl", "wb") as f:
    pickle.dump(onehot_encoders, f)

# Train the XGBoost model
model = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=6, random_state=42)
model.fit(X_train, y_train)

# Validate the model
y_pred = model.predict(X_valid)
accuracy = accuracy_score(y_valid, y_pred)
print(f"Validation Accuracy: {accuracy:.4f}")

# Save the trained model
with open("saved_models/email_classifier.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully.")

