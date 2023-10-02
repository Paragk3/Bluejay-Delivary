import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('Assignment_Timecard.xlsx')

# Ensure 'Time' column is in datetime format
df['Time'] = pd.to_datetime(df['Time'])

# Sort the DataFrame by 'Employee Name' and 'Time' to ensure consecutive days are grouped together
df.sort_values(by=['Employee Name', 'Time'], inplace=True)

# Calculate the time difference between consecutive rows for each employee
df['TimeDiff'] = df.groupby('Employee Name')['Time'].diff()

# Initialize lists to store employees who meet the criteria
employees_7_consecutive_days = []
employees_less_than_10_hours = []
employees_more_than_14_hours = []

# Iterate through the DataFrame to find employees who meet the criteria
for index, row in df.iterrows():
    if row['TimeDiff'] == pd.Timedelta(days=1):
        if row['Employee Name'] not in employees_7_consecutive_days:
            employees_7_consecutive_days.append(row['Employee Name'])
    if (row['TimeDiff'] >= pd.Timedelta(hours=1)) and (row['TimeDiff'] < pd.Timedelta(hours=10)):
        if row['Employee Name'] not in employees_less_than_10_hours:
            employees_less_than_10_hours.append(row['Employee Name'])
    try:
        timecard_hours = float(row['Timecard Hours (as Time)'])
        if timecard_hours > 14:
            if row['Employee Name'] not in employees_more_than_14_hours:
                employees_more_than_14_hours.append(row['Employee Name'])
    except ValueError:
        pass

# Print the name and position of employees who meet the criteria
print("Employees who have worked for 7 consecutive days:")
for employee in employees_7_consecutive_days:
    print(f"Name: {employee}, Position ID: {df[df['Employee Name'] == employee]['Position ID'].iloc[0]}")

print("\nEmployees who have less than 10 hours between shifts:")
for employee in employees_less_than_10_hours:
    print(f"Name: {employee}, Position ID: {df[df['Employee Name'] == employee]['Position ID'].iloc[0]}")

print("\nEmployees who have worked for more than 14 hours in a single shift:")
for employee in employees_more_than_14_hours:
    print(f"Name: {employee}, Position ID: {df[df['Employee Name'] == employee]['Position ID'].iloc[0]}")
