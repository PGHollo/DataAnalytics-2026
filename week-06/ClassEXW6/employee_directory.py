class Employee:

    company = "DataPlus Analytics"

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary 

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")

    def annual_bonus(self):
        bonus = self.salary * 0.10
        print(f"Annual Bonus: ${bonus:,.2f}")
