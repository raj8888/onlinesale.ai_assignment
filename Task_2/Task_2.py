import csv

# Function to read CSV file and return data as a list of dictionaries
def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Read Departments CSV
departments = read_csv_file('../Data/Departments.csv')

# Read Employees CSV
employees = read_csv_file('../Data/Employees.csv')

# Read Salaries CSV
salaries = read_csv_file('../Data/Salaries.csv')

# Dictionary to store department-wise salary totals and counts
department_totals = {}
department_counts = {}

# Calculate department-wise salary totals and counts
for salary in salaries:
    employee_id = salary['EMP_ID']
    amount = float(salary['AMT'])

    for employee in employees:
        if employee['ID'] == employee_id:
            department_id = employee['DEPT_ID']
            break

    for department in departments:
        if department['ID'] == department_id:
            department_name = department['NAME']
            break

    department_totals.setdefault(department_name, 0)
    department_totals[department_name] += amount

    department_counts.setdefault(department_name, 0)
    department_counts[department_name] += 1

# Calculate average monthly salary for each department
department_avg_salaries = {
    department: department_totals[department] / department_counts[department]
    for department in department_totals
}

# Sort departments by average monthly salary in descending order
top_departments = sorted(
    department_avg_salaries.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

# Write the report to a file
with open('Task_2_Report.txt', 'w') as file:
    file.write("{:<15}{}\n".format("DEPT_NAME", "AVG_MONTHLY_SALARY (USD)"))
    file.write("-" * 40 + "\n")
    for department, avg_salary in top_departments:
        file.write("{:<15}{:.2f} (USD)\n".format(department, avg_salary))

# Check Task_2_Report.txt file for output.