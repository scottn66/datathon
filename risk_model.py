import pandas as pd
from sklearn.linear_model import LogisticRegression
from tqdm import tqdm

s = pd.read_csv("subsidy_tracker_clean.csv")
v = pd.read_csv("ViolationTracker_basic clean.csv")

print(s.shape)
print(v.shape)

violating_companies = set(v['company'])
print(len(violating_companies))
subsidy_companies = set(s['company'])
print(len(subsidy_companies))

intersection = violating_companies.intersection(subsidy_companies)
print(len(intersection))

s_companies = s['company']
viol_bool = []

for c in tqdm(s_companies):
    if c in intersection:
        viol_bool.append(1)
    else:
        viol_bool.append(0)

print(sum(viol_bool) / len(viol_bool))
print(sum(viol_bool))
print(len(viol_bool))

s['VIOLATION'] = viol_bool

print(s.head())

print(s.columns)
categorical_dict = {}
for c in s.columns:
    unique_values = s[c].unique()
    categorical_dict[c] = unique_values

for c, unique_values in categorical_dict.items():
    print(c, len(unique_values))
    print("\n")






















































import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix



# Define continuous and categorical columns
continuous_columns = ['subsidy', 'subsidy_adjusted']
categorical_columns = ['state', 'program', 'subsidy_type', 'agency', 'sub_year', 'subsidy_level']



# Preprocess continuous variables
X_continuous = s[continuous_columns]
scaler = StandardScaler()
X_continuous_scaled = scaler.fit_transform(X_continuous)

# Preprocess categorical variables
X_categorical = s[categorical_columns]
encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
X_categorical_encoded = encoder.fit_transform(X_categorical)

# Combine continuous and categorical variables
X = pd.concat([pd.DataFrame(X_continuous_scaled, columns=continuous_columns), 
               pd.DataFrame(X_categorical_encoded, columns=encoder.get_feature_names_out(categorical_columns))], axis=1)
y = s['VIOLATION']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tqdm import tqdm


# Custom callback function for tqdm
class TqdmCallback:
    def __init__(self, total_iterations):
        self.total_iterations = total_iterations
        self.progress_bar = tqdm(total=total_iterations, desc="Training progress")

    def __call__(self, k, loss):
        self.progress_bar.update(1)

    def close(self):
        self.progress_bar.close()



# Define continuous and categorical columns
continuous_columns = ['subsidy', 'subsidy_adjusted']
categorical_columns = ['state', 'program', 'subsidy_type', 'agency']

# Preprocess continuous variables
X_continuous = s[continuous_columns]
scaler = StandardScaler()
X_continuous_scaled = scaler.fit_transform(X_continuous)

# Preprocess categorical variables
X_categorical = s[categorical_columns]
encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
X_categorical_encoded = encoder.fit_transform(X_categorical)

# Combine continuous and categorical variables
X = pd.concat([pd.DataFrame(X_continuous_scaled, columns=continuous_columns), 
               pd.DataFrame(X_categorical_encoded, columns=encoder.get_feature_names_out(categorical_columns))], axis=1)
y = s['VIOLATION']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the logistic regression model
log_reg = LogisticRegression(solver='saga', max_iter=1000)
callback = TqdmCallback(total_iterations=log_reg.max_iter)

log_reg.set_params(callback=callback)
log_reg.fit(X_train, y_train)

callback.close()

# Make predictions on the test set
y_pred = log_reg.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Classification report:")
print(classification_report(y_test, y_pred))

print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))
