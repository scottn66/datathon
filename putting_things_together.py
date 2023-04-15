import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


common_subsidy = pd.read_csv("common_subsidy.csv")
common_violations = pd.read_csv("common_violations.csv")

print("subsidy shape: ", common_subsidy.shape)

print("violations shape: ", common_violations.shape)

"""
Trimming down 
"""

common_subsidy = common_subsidy[['company','state', 'program', 'subsidy_type', 'agency', 'sub_year',
                                 'major_industry','industry','parent_name',
                                 'unique_id','subsidy_level']]

common_violations = common_violations[['company', 'naics_tr','penalty_date','civil_criminal','description', 'offense_group']]
viol1 = common_violations.rename(columns={'company':'Company'})

df = common_subsidy.merge(viol1, left_on='company', right_on='Company')

# print(f"common_subsidy.columns: {common_subsidy.columns}")
# print("subsidy shape: ", common_subsidy.shape)
# print("violations shape: ", common_violations.shape)
# print("\n\n\n")
# print(common_subsidy.head())
# print(common_violations.head())
# print("\n\n\n")
# print("\n\n\n")
# print(df)
# print(df.columns)
# #df.to_csv('joined_subsidy_violation.csv')
# print(df.describe())



# Separate categorical and continuous variables
categorical_vars = []
continuous_vars = []

for col in df.columns:
    if df[col].dtype == 'object' or df[col].dtype.name == 'category':
        categorical_vars.append(col)
    elif df[col].dtype == 'int64' or df[col].dtype == 'float64':
        continuous_vars.append(col)

print("Categorical variables:", categorical_vars)
print("Continuous variables:", continuous_vars)


subsid_type = list(df['subsidy_type'])
unique_sub_types = list(set(subsid_type))

violation_type = list(df['offense_group'])
unique_violation_types = list(set(violation_type))

print("\nTHESE SHOULD BE THE SAME: ")
print(len(subsid_type), len(violation_type))

print("\nUnique sub types: " , len(unique_sub_types))
print("\nUnique violation types: " , len(unique_violation_types))


# Plot the categorical variables
# value_counts = df['agency'].value_counts()

# List of categorical columns
categorical_columns = ['company', 'state', 'program', 'subsidy_type', 'agency', 'major_industry', 'industry', 'parent_name', 'subsidy_level', 'Company', 'naics_tr', 'civil_criminal', 'description']

# Initialize an empty dictionary to store the frequency counts
frequency_dict = {}

# Loop through the categorical columns and calculate the frequency counts
for column in categorical_columns:
    frequency_dict[column] = df[column].value_counts().to_dict()

# Print the frequency dictionary
print(frequency_dict)

