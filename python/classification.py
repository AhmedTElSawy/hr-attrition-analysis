import pandas as pd

file_name = "GBS BI HUB - BI Developer - HR Attrition Case Study.xlsx"
sheet_name = "Employee Data"

df = pd.read_excel(file_name, sheet_name)

# Classify experience levels using a list comprehension
df['ExperienceLevel'] = [
        'Junior' if x < 5 
    else 'Mid' if x <= 9 
    else 'Senior' 
    for x in df['TotalWorkingYears']]

# Generate summary table
summary_table = df.groupby('ExperienceLevel').size().reset_index(name='EmployeeCount')

# Display summary table
print(summary_table)

'''
Can use pd.cut() for larger datasets (vectorization)

df['ExperienceLevel'] = pd.cut(
    df['TotalWorkingYears'], 
    bins=[-1, 4, 9, float('inf')], 
    labels=['Junior', 'Mid', 'Senior']
)
'''