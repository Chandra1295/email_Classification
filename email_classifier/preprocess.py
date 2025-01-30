import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

def handle_outliers(df, feature):
    """Cap outliers using the IQR method."""
    IQR = df[feature].quantile(0.75) - df[feature].quantile(0.25)
    lower_limit = df[feature].quantile(0.25) - (IQR * 1.5)
    upper_limit = df[feature].quantile(0.75) + (IQR * 1.5)

    df[feature] = np.where(df[feature] > upper_limit, upper_limit, df[feature])
    df[feature] = np.where(df[feature] < lower_limit, lower_limit, df[feature])
    
    return df[feature]

def preprocess_data(data, is_train=True):
    """Preprocess training or testing data and return processed X, y along with fitted scalers and encoders."""
    
    # Drop unnecessary columns from the data
    columns_to_drop = ['campaign_id', 'click_rate', 'is_personalised', 'is_timer',
                       'is_emoticons', 'is_discount', 'is_price', 'is_urgency',
                       'sender', 'target_audience']
    data = data.drop(columns=[col for col in columns_to_drop if col in data.columns], errors='ignore')

    # Handle outliers (if needed for test data as well)
    outlier_features = ['no_of_CTA', 'mean_paragraph_len', 'body_len', 'subject_len', 'mean_CTA_len']
    for feature in outlier_features:
        data[feature] = handle_outliers(data, feature)

    # One-hot encoding for categorical columns
    onehot_features = ['is_weekend', 'day_of_week', 'times_of_day']
    onehot_encoders = {}

    for feature in onehot_features:
        if feature in data.columns:
            encoder = onehot_encoders.get(feature, None)
            if encoder is None:
                encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
                encoded_data = encoder.fit_transform(data[[feature]])
                onehot_encoders[feature] = encoder

            data = data.drop(columns=[feature])
            data = data.join(pd.DataFrame(encoded_data, 
                                          columns=encoder.get_feature_names_out([feature]), 
                                          index=data.index))
        else:
            print(f"Warning: {feature} column is missing from the data.")

    # If it's training data, separate features and target ('clicked')
    if is_train:
        X = data.drop(columns=['clicked'], errors='ignore')
        y = data['clicked']
        return X, y, onehot_encoders
    else:
        # If it's test/predict data, only return the features
        X = data
        return X, None, onehot_encoders

