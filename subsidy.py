import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


subsidy = pd.read_csv('subsidy_tracker_clean.csv')
subsidy_basic = pd.read_csv('subsidy_tracker_202321feb_basic.csv')
subsidy_parent = pd.read_csv('subsidy_tracker_202321feb_parent.csv')

print(f"subsidy shape & columns: {subsidy.shape} {subsidy.columns}")
print(f"subsidy_basic.columns: {subsidy_basic.shape} {subsidy_basic.columns}")
print(f"subsidy_parent.columns: {subsidy_parent.shape} {subsidy_parent.columns}")

industry_distribution = subsidy.groupby('major_industry')['subsidy_adjusted'].sum()

industry_distribution = industry_distribution.sort_values(ascending=False)

cutoff_percentage = 2  # You can change this percentage to control the number of smaller values to display in the table
cutoff_value = industry_distribution.sum() * cutoff_percentage / 100
larger_values = industry_distribution[industry_distribution >= cutoff_value]
smaller_values = industry_distribution[industry_distribution < cutoff_value]

other_sum = smaller_values.sum()
larger_values_with_other = larger_values.append(pd.Series({'Other': other_sum}))

plt.figure(figsize=(10, 10))
larger_values_with_other.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Subsidies per Industry (including 'Other' category)")
plt.ylabel("")  # To remove the default y-axis label
plt.tight_layout()
plt.show()




# plt.figure(figsize=(10, 10))
# larger_values.plot.pie(autopct='%1.1f%%', startangle=90)
# plt.title("Distribution of Subsidies per Industry (Larger Slices)")
# plt.ylabel("")  # To remove the default y-axis label
# plt.tight_layout()
# plt.show()

smaller_values_table = pd.DataFrame(smaller_values).reset_index()
smaller_values_table.columns = ['Industry', 'Subsidy Amount']
smaller_values_table['Percentage'] = (smaller_values_table['Subsidy Amount'] / industry_distribution.sum()) * 100
print(smaller_values_table)


################################## distrubution of subsidies across company sizes############################################

# Group the data by company and sum the subsidies
company_subsidy = subsidy_basic.groupby('company')['subsidy'].sum().reset_index()

# Sort the companies by the total subsidies received
company_subsidy = company_subsidy.sort_values('subsidy', ascending=False)

# Display the top 10 companies with the highest subsidies
print(company_subsidy.head(10))

# Define the size categories using quantiles
small_threshold = company_subsidy['subsidy'].quantile(0.25)
medium_threshold = company_subsidy['subsidy'].quantile(0.75)

# Create a function to assign the size category based on the total subsidies
def assign_size_category(row):
    if row['subsidy'] <= small_threshold:
        return 'small'
    elif row['subsidy'] <= medium_threshold:
        return 'medium'
    else:
        return 'large'

# Apply the size category function to each row in the company_subsidy DataFrame
company_subsidy['size_category'] = company_subsidy.apply(assign_size_category, axis=1)

# Display the company_subsidy DataFrame with the new size_category column
print(company_subsidy.head())


# Group the data by size_category and sum the subsidies
size_distribution = company_subsidy.groupby('size_category')['subsidy'].sum().reset_index()

# Create a bar chart of the total subsidies for each size category
plt.figure(figsize=(8, 6))
sns.barplot(x='size_category', y='subsidy', data=size_distribution)
plt.title('Subsidy Distribution by Company Size')
plt.xlabel('Company Size')
plt.ylabel('Total Subsidies')
plt.show()






"""
    Analyze the allocation and impact of economic development subsidies:
        Identify the distribution of subsidies across industries, regions, and company sizes.
        Assess the effectiveness of subsidies in terms of job creation, economic growth, and other key performance indicators.
        Identify the factors that contribute to the success or failure of subsidy programs.

    Assess the relationship between subsidy receipt and instances of corporate misconduct:
        Analyze the correlation between companies receiving subsidies and the frequency or severity of violations.
        Investigate if certain industries or regions are more prone to misconduct after receiving subsidies.
        Explore any trends in the type of violations committed by companies receiving subsidies.

    Identify implications for community well-being and socioeconomic outcomes:
        Analyze the impact of subsidy programs on local communities in terms of employment, income, education, and other socioeconomic indicators.
        Assess whether subsidies have any unintended consequences, such as increased inequality or environmental degradation.
        Explore the long-term effects of subsidies on community resilience and economic sustainability.

    Communicate insights effectively:
        Present your findings in a clear and concise manner, using visual aids such as charts, graphs, and maps to help stakeholders understand the data.
        Focus on the key insights that directly relate to the stakeholders' objectives and can drive decision-making.

    Provide recommendations:
        Based on your insights, suggest improvements to subsidy allocation and monitoring processes to ensure that they are more effective and better aligned with the desired outcomes.
        Recommend strategies for mitigating the risks of corporate misconduct and enhancing community well-being.
        Propose ways to measure and track the impact of subsidies on communities and the economy over time.

    Encourage discussion and feedback:
        Engage with stakeholders to discuss your findings and recommendations, and solicit their input and perspectives.
        Refine your analysis based on stakeholder feedback to ensure that your insights align with their needs and expectations.

        
    Construction: The construction industry generates demand for materials, labor, and various services, including design, engineering, and legal services. As a result, an increase in construction activity can have a significant impact on other industries, creating a strong multiplier effect.

    Manufacturing: Manufacturing industries often have high multiplier effects due to their extensive supply chains and the need for various inputs such as raw materials, labor, and energy. An increase in manufacturing demand can lead to increased production in related industries.

    Infrastructure and utilities: Investments in infrastructure and utilities, such as transportation, energy, and telecommunications, can have a high multiplier effect, as they create demand for construction, maintenance, and other services, while also improving the productivity and efficiency of other industries.

    Tourism and hospitality: The tourism and hospitality industry can have a significant multiplier effect on local economies, as tourists spend money on accommodation, food, transportation, and other services, supporting local businesses and creating employment opportunities.

    Health care and social services: The health care and social services sector generates demand for a wide range of goods and services, including pharmaceuticals, medical devices, and professional services. This demand can lead to a high multiplier effect, as increased spending in health care supports various other industries.
        
        
    """
