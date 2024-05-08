

def add_employee(employees, name, emp_id, department, salary):
    """
    Add a new employee to the database.

    Parameters:
    employees (list): List representing the employee database.
    name (str): Name of the employee.
    emp_id (int): Employee ID.
    department (str): Department of the employee.
    salary (float): Salary of the employee.
    """
    for employee in employees:
        if employee['emp_id'] == emp_id:
            print("Employee with the same ID already exists.")
            return
    if salary < 0:
        print("Salary cannot be negative.")
        return
    employees.append({'name': name, 'emp_id': emp_id, 'department': department, 'salary': salary})
    print(f"Employee added successfully. => Name: {name}, ID: {emp_id}, Department: {department}, Salary: {salary}")
    

def update_employee(employees, emp_id, department=None, salary=None):
    """
    Update employee information.

    Parameters:
    employees (list): List representing the employee database.
    emp_id (int): Employee ID to update.
    department (str, optional): New department of the employee.
    salary (float, optional): New salary of the employee.
    """
    for employee in employees:
        if employee['emp_id'] == emp_id:
            if department is not None:
                employee['department'] = department
            if salary is not None:
                if salary < 0:
                    print("Salary cannot be negative.")
                    return
                employee['salary'] = salary
            print(f"Employee information updated successfully. => Employee Id: {emp_id}, Department: {department}, Salary: {salary}")
            return
    print("Employee ID not found.")

def generate_report(employees, department=None, sorted_by_salary=False):
    """
    Generate a report listing all employees and their details.

    Parameters:
    employees (list): List representing the employee database.
    department (str, optional): Filter employees by department.
    sorted_by_salary (bool, optional): Whether to sort employees by salary.

    Returns:
    list: List of employees matching the criteria.
    """
    if department is not None:
        filtered_employees = [emp for emp in employees if emp['department'] == department]
    else:
        filtered_employees = employees

    if sorted_by_salary:
        filtered_employees.sort(key=lambda x: x['salary'])

    return filtered_employees

# Sample usage:
employees_db = []

# Add employees
add_employee(employees_db, "Ahmed Mahdy", 1001, "HR", 50000)
add_employee(employees_db, "Omer Mohamed", 1002, "Finance", 60000)
add_employee(employees_db, "Alaa Ahmed", 1003, "Marketing", 55000)

# # Update employee information
update_employee(employees_db, 1002, salary=62000)
update_employee(employees_db, 1004)  # This should print "Employee ID not found."

# # Generate employee report
report = generate_report(employees_db)
print("Employee Report:")
for emp in report:
    print(f"Name: {emp['name']}, ID: {emp['emp_id']}, Department: {emp['department']}, Salary: ${emp['salary']}")

