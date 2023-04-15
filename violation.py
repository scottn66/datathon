import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

v = pd.read_csv('ViolationTracker_basic_28feb23.csv')
violations = pd.read_csv('ViolationTracker_basic_clean.csv')
violations_parent = pd.read_csv('ViolationTracker_current_parents_28feb23.csv')
violations_public_parent = pd.read_csv('ViolationTracker_reporting_date_public_parents_28feb23.csv')

print(f"v shape & columns: {v.shape} {v.columns}")
print(f"violations shape & columns: {violations.shape} {violations.columns}")
print(f"violations_parent.columns: {violations_parent.shape} {violations_parent.columns}")
print(f"violations_public_parent.columns: {violations_public_parent.shape} {violations_public_parent.columns}")


# Group the data by company and count the number of violations
company_violations = violations.groupby('company')['unique_id'].count().reset_index()

# Rename the 'unique_id' column to 'violation_count'
company_violations.columns = ['company', 'violation_count']

# Sort the companies by the number of violations
company_violations = company_violations.sort_values('violation_count', ascending=False)

# Display the top 10 companies with the highest number of violations
print(company_violations.head(10))

# Create a bar chart of the top 10 companies with the highest number of violations
plt.figure(figsize=(12, 6))
sns.barplot(x='company', y='violation_count', data=company_violations.head(10))
plt.title('Top 10 Companies with the Highest Number of Violations')
plt.xlabel('Company')
plt.ylabel('Number of Violations')
plt.xticks(rotation=45)
plt.show()



# Group the data by company and violation year, and count the number of violations
company_year_violations = (
    violations.groupby(['company', 'pen_year'])['unique_id']
    .count()
    .reset_index()
)

# Rename the 'unique_id' column to 'violation_count'
company_year_violations.columns = ['company', 'violation_year', 'violation_count']

# Sort the data by the number of violations in descending order
company_year_violations = company_year_violations.sort_values(
    'violation_count', ascending=False
)

# Display the violations per company per year
print(company_year_violations)



# Group the data by violation year and count the number of violations
year_violations = (
    violations.groupby('pen_year')['unique_id']
    .count()
    .reset_index()
)

# Rename the 'unique_id' column to 'violation_count'
year_violations.columns = ['violation_year', 'violation_count']

# Sort the data by the violation year
year_violations = year_violations.sort_values('violation_year')

# Plot the violations per year using a bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='violation_year', y='violation_count', data=year_violations)
plt.title('Violations per Year')
plt.xlabel('Year')
plt.ylabel('Number of Violations')
plt.xticks(rotation=45)
plt.show()


# Group the data by violation year and sum the penalty_adjusted column
year_violation_severity = (
    violations.groupby('pen_year')['penalty_adjusted']
    .sum()
    .reset_index()
)

# Rename the 'penalty_adjusted' column to 'total_severity'
year_violation_severity.columns = ['violation_year', 'total_severity']

# Sort the data by the violation year
year_violation_severity = year_violation_severity.sort_values('violation_year')

# Plot the total violation severity per year using a bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='violation_year', y='total_severity', data=year_violation_severity)
plt.title('Total Violation Severity per Year')
plt.xlabel('Year')
plt.ylabel('Total Violation Severity')
plt.xticks(rotation=45)
plt.show()