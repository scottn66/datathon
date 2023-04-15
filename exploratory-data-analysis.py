import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import pickle

subsidy = pd.read_csv('subsidy_tracker_clean.csv')
violations = pd.read_csv('ViolationTracker_basic clean.csv')

print("subsidy shape: ", subsidy.shape)
print("violations shape: ", violations.shape)

print("subsidy columns: ", subsidy.columns)
print("violations coumns: ",violations.columns)


"""
Missing columns info below
"""
def missing_column_report(df):
    cols = df.columns
    missing_dict = {}
    for c in cols:
        c_df = df[c]
        pre_len = c_df.shape[0]
        post_len = c_df[c_df.notnull()].shape[0]
        missing_dict[c] = pre_len - post_len
    return missing_dict

# missing_subsidy_columns = missing_column_report(subsidy)
# missing_violations_columns = missing_column_report(violations)

# pprint(missing_subsidy_columns)
# pprint(missing_violations_columns)

# print("FEWEST MISSING VALUES FIRST, SUBSIDY: ", sorted(missing_subsidy_columns))
# print("FEWEST MISSING VALUES FIRST, VIOLATIONS: ", sorted(missing_violations_columns))

# plt.bar(range(len(missing_subsidy_columns)), list(missing_subsidy_columns.values()))
# plt.show()

# plt.bar(range(len(missing_violations_columns)), list(missing_violations_columns.values()))
# plt.show()

"""
Checking overlap between df's
"""
companies_subsidy = list(set(subsidy['company']))
companies_violations = list(set(violations['company']))

print("Num unique subsidy companies: ", len(companies_subsidy))
print("Num unique violations companies: ", len(companies_violations))

# company_intersection = set(companies_subsidy).intersection(set(companies_violations))
# print("Num unique companies in both subsidy and violations: ", len(company_intersection))
"""
Num unique subsidy companies:     407966
Num unique violations companies:  401682
Num companies in BOTH:              9525
"""

# with open("company_intersection.bin", "wb") as f: # "wb" because we want to write in binary mode
#     pickle.dump(company_intersection, f)


# Find overlapping columns
# overlapping_columns = set(subsidy.columns).intersection(set(violations.columns))
# print("Overlapping columns:", overlapping_columns)
"""
Overlapping columns: {'info_source', 'company', 'notes', 'county', 'load_day', 
'street_address', 'state', 'unique_id', 'zip', 'naics', 'description', 'agency', 'city'}

"""



