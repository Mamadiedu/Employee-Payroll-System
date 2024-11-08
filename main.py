# Base class for all employees
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        raise NotImplementedError("Subclasses must implement this method")


# Derived class for salaried employees
class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


# Derived class for hourly employees
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


# Derived class for commission-based employees
class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission):
        super().__init__(emp_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return self.weekly_salary + self.commission


# Example usage
salary_employee = SalaryEmployee(1, "John Doe", 1500)
hourly_employee = HourlyEmployee(2, "Jane Smith", 40, 20)
commission_employee = CommissionEmployee(3, "Alice Brown", 1000, 500)

print("Salary Employee Payroll:", salary_employee.calculate_payroll())
print("Hourly Employee Payroll:", hourly_employee.calculate_payroll())
print("Commission Employee Payroll:", commission_employee.calculate_payroll())
