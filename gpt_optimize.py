import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV files
common_subsidy = pd.read_csv("common_subsidy.csv")
common_violations = pd.read_csv("common_violations.csv")

# Select relevant columns from the DataFrames
common_subsidy = common_subsidy[['company', 'state', 'program', 'subsidy_type', 'agency', 'sub_year', 'major_industry', 'industry', 'parent_name', 'unique_id', 'subsidy_level']]
common_violations = common_violations[['company', 'state','naics_tr', 'penalty_date', 'civil_criminal', 'description', 'offense_group']]



##################### for merged df #####################

# Rename 'company' column in common_violations and merge DataFrames
common_violations = common_violations.rename(columns={'company': 'Company'})
df = common_subsidy.merge(common_violations, left_on='company', right_on='Company')
common_violations = common_violations.rename(columns={'Company': 'company', 'naics_tr': 'industry'})


# Separate categorical and continuous variables
df_categorical_vars = [col for col in df.columns if df[col].dtype == 'object' or df[col].dtype.name == 'category']
df_continuous_vars = [col for col in df.columns if df[col].dtype == 'int64' or df[col].dtype == 'float64']

print("Categorical variables:", df_categorical_vars)
print("Continuous variables:", df_continuous_vars)

# Create frequency dictionary for categorical variables
df_frequency_dict = {column: df[column].value_counts().to_dict() for column in df_categorical_vars}

# Print the frequency dictionary
print(df_frequency_dict)




################### for just subsidy df ####################

# Separate categorical and continuous variables
sub_categorical_vars = [col for col in common_subsidy.columns if common_subsidy[col].dtype == 'object' or common_subsidy[col].dtype.name == 'category']
sub_continuous_vars = [col for col in common_subsidy.columns if common_subsidy[col].dtype == 'int64' or common_subsidy[col].dtype == 'float64']

print("Categorical variables:", sub_categorical_vars)
print("Continuous variables:", sub_continuous_vars)

# Create frequency dictionary for categorical variables
sub_frequency_dict = {column: common_subsidy[column].value_counts().to_dict() for column in sub_categorical_vars}

# Print the frequency dictionary
print(sub_frequency_dict)




################### for just violation df ####################

# Separate categorical and continuous variables
viol_categorical_vars = [col for col in common_violations.columns if common_violations[col].dtype == 'object' or common_violations[col].dtype.name == 'category']
viol_continuous_vars = [col for col in common_violations.columns if common_violations[col].dtype == 'int64' or common_violations[col].dtype == 'float64']

print("Violation Categorical variables:", viol_categorical_vars)
print("Violation Continuous variables:", viol_continuous_vars)

# Create frequency dictionary for categorical variables
viol_frequency_dict = {column: common_violations[column].value_counts().to_dict() for column in viol_categorical_vars}

# Print the frequency dictionary
print(viol_frequency_dict)



# Function to plot the frequency dictionary
def plot_frequency_dict(frequency_dict, column):
    keys = list(frequency_dict[column].keys())
    values = list(frequency_dict[column].values())
    
    plt.figure(figsize=(10, 5))
    plt.bar(keys, values)
    plt.xticks(rotation=90)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Frequency Distribution of {column}')
    plt.show()

# # Iterate through each categorical variable and plot the frequency distribution
# for column in df_categorical_vars:
#     plot_frequency_dict(df_frequency_dict, column)


for column in viol_categorical_vars:
    plot_frequency_dict(viol_frequency_dict, column)