import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('Assignment_Timecard.xlsx')

# Sort the DataFrame by 'Employee Name' and 'Time' to ensure consecutive days are grouped together
df.sort_values(by=['Employee Name', 'Time'], inplace=True)

# Calculate the time difference between consecutive rows for each employee
df['TimeDiff'] = df.groupby('Employee Name')['Time'].diff()

# Condition (a): Employees who have worked for 7 consecutive days
consecutive_days = df[df['TimeDiff'] == pd.Timedelta(days=1)]['Employee Name'].value_counts()
employees_7_consecutive_days = consecutive_days[consecutive_days == 6].index.tolist()

# Clean and convert the 'Timecard Hours (as Time)' column to numeric
df['Timecard Hours (as Time)'] = df['Timecard Hours (as Time)'].str.extract(r'(\d+\.\d+)').astype(float)

# Condition (b): Employees who have less than 10 hours of time between shifts but greater than 1 hour
condition_b = (df['TimeDiff'] > pd.Timedelta(hours=1)) & (df['TimeDiff'] < pd.Timedelta(hours=10))

# Condition (c): Employees who have worked for more than 14 hours in a single shift
condition_c = df['Timecard Hours (as Time)'] > 14

# Filter the DataFrame based on conditions (b) and (c) and the list of employees with 7 consecutive days
filtered_df = df[(condition_b | condition_c) & df['Employee Name'].isin(employees_7_consecutive_days)]

# Print the name and position of employees who meet the criteria
for index, row in filtered_df.iterrows():
    print(f"Name: {row['Employee Name']}, Position ID: {row['Position ID']}")
