import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
s = pd.read_csv("subsidy_tracker_clean.csv")

# Select the relevant features and target
categorical_columns = ['state', 'program', 'subsidy_type', 'agency', 'sub_year', 'company', 
                       'city', 'county', 'street_address', 'zip', 'major_industry', 'industry', 
                       'description', 'naics', 'jobs_data', 'wage_data', 'wage_data_type', 
                       'investment_data', 'info_source', 'notes', 'subsidy', 'subsidy_adjusted', 
                       'megadeal_contrib', 'subsidy_display', 'parent_name', 'unique_id', 'load_day', 
                       'subsidy_level', 'cfda_program_num', 'face_loan', 'principal_place_state_code', 
                       'principal_place_code', 'principal_place_cc', 'principal_place_zip', 
                       'unique_transaction_id', 'duns', 'last_mod_date']
X = s[categorical_columns]
y = s['VIOLATION']

# One-hot encode the categorical features
encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
X_encoded = encoder.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Create and fit the logistic regression model
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = log_reg.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Classification report:")
print(classification_report(y_test, y_pred))

print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))
