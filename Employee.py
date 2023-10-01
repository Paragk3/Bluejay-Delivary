# Define a function to check consecutive days worked
from django.forms import FilePathField


def check_consecutive_days(days_worked):
    return '1111111' in days_worked

# Define a function to analyze the file
def analyze_employee_file(file_path):
    # Specify the path to your input file
     
    
    with open(FilePathField, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            Employee_Name = data[0]
            Position_ID = data[1]
            days_worked = data[2]
            time_between_shifts = int(data[3])
            total_hours_worked = int(data[4])

            if check_consecutive_days(days_worked):
                print(f"A. Name: {Employee_Name}, Position: {Position_ID}")

            if time_between_shifts > 1 and time_between_shifts <= 24:
                print(f"B. Name: {Employee_Name}, Position: {Position_ID}")

            if total_hours_worked > 14:
                print(f"C. Name: {Employee_Name}, Position: {Position_ID}")

        file_path = 'Assignment_Timecard.xlsx'
        analyze_employee_file(new_func(file_path))

def new_func(file_path):
    return file_path

