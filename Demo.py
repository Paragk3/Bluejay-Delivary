import openpyxl

from Employee import check_consecutive_days

def analyze_employee_file(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2):
        name = row[0].value
        position = row[1].value
        days_worked = row[2].value
        time_between_shifts = int(row[3].value)
        total_hours_worked = int(row[4].value)

        if check_consecutive_days(days_worked):
            print(f"A. Name: {name}, Position: {position}")

        if time_between_shifts > 1 and time_between_shifts <= 24:
            print(f"B. Name: {name}, Position: {position}")

        if total_hours_worked > 14:
            print(f"C. Name: {name}, Position: {position}")

file_path = 'Assignment_Timecard.xlsx'
analyze_employee_file(file_path)