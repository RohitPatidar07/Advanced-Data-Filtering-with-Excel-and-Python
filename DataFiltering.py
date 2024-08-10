 
import pandas as pd
import os
 
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown', 'Sarah Davis', 'David Wilson', 'Linda Martinez', 'James Anderson', 'Karen Thomas', 'Robert Taylor'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Marketing', 'Finance', 'IT', 'Marketing'],
    'Position': ['Developer', 'Manager', 'Developer', 'Analyst', 'Coordinator', 'Manager', 'Specialist', 'Manager', 'Developer', 'Manager'],
    'HireDate': ['2020-01-15', '2018-03-22', '2019-07-30', '2017-05-10', '2021-09-12', '2016-11-25', '2019-01-14', '2015-08-18', '2022-02-19', '2020-12-01'],
    'Salary': [70000, 80000, 72000, 68000, 52000, 95000, 60000, 87000, 71000, 85000],
    'Location': ['New York', 'Chicago', 'New York', 'Boston', 'Chicago', 'New York', 'Boston', 'Boston', 'New York', 'Chicago']
}
 
df = pd.DataFrame(data)
 
file_path = 'EmployeeData.xlsx'
 
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='OriginalData', index=False)
 
df = pd.read_excel(file_path, sheet_name='OriginalData')

print("Original DataFrame:")
print(df.head())
 
basic_filter = df.query("Department == 'IT'")
conditional_filter = df.query("Salary > 70000")
multi_condition_filter = df.query("Department == 'IT' and Salary > 70000")
groupby_filter = df.groupby('Department').filter(lambda x: len(x) > 2)
regex_filter = df[df['Position'].str.contains(r'Manager', case=False, na=False)]
 
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
    basic_filter.to_excel(writer, sheet_name='Basic_Filter', index=False)
    conditional_filter.to_excel(writer, sheet_name='Conditional_Filter', index=False)
    multi_condition_filter.to_excel(writer, sheet_name='Multi_Condition_Filter', index=False)
    groupby_filter.to_excel(writer, sheet_name='GroupBy_Filter', index=False)
    regex_filter.to_excel(writer, sheet_name='Regex_Filter', index=False)

print(f"\nFiltered data has been written to '{file_path}'")
