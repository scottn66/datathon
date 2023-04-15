import pandas as pd
import pickle
from pprint import pprint
import re
from tqdm import tqdm

subsidy = pd.read_csv('subsidy_tracker_clean.csv')
violations = pd.read_csv('ViolationTracker_basic clean.csv')

industry_names = list(set(violations['naics_tr']))
for i in tqdm(range(len(industry_names))):
    industry_names[i] = re.sub(r'\d+: ', '', str(industry_names[i]))

print(list(set(industry_names)))


with open("company_intersection.bin", "rb") as f: # "rb" because we want to read in binary mode
    company_intersection = list(pickle.load(f))

print(f"Num companies in BOTH: {len(company_intersection)}")
#print(f"companies in BOTH: {company_intersection}")
#pprint(company_intersection)

subsidy_subset = subsidy[subsidy['company'].isin(company_intersection)]
violations_subset = violations[violations['company'].isin(company_intersection)]

print("shapes: ", subsidy_subset.shape, violations_subset.shape)

subsidy_subset.to_csv('common_subsidy.csv')
violations_subset.to_csv('common_violations.csv')