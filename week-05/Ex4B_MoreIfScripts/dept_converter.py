"""Convert a department code into a department name using if/elif/else."""

department_code = int(input("Enter the department code: "))

if department_code == 1:
    department_name = "Marketing"
elif department_code == 5:
    department_name = "Human Resources"
elif department_code == 10:
    department_name = "Accounting"
elif department_code == 12:
    department_name = "Legal"
elif department_code == 18:
    department_name = "IT"
elif department_code == 20:
    department_name = "Customer Relations"
else:
    department_name = "Invalid department code"

print(f"Department code: {department_code}")
print(f"Department name: {department_name}")




"""Convert a department code into a department name using match/case."""

department_code = int(input("Enter the department code: "))

match department_code:
    case 1:
        department_name = "Marketing"
    case 5:
        department_name = "Human Resources"
    case 10:
        department_name = "Accounting"
    case 12:
        department_name = "Legal"
    case 18:
        department_name = "IT"
    case 20:
        department_name = "Customer Relations"
    case _:
        department_name = "Invalid department code"

print(f"Department code: {department_code}")
print(f"Department name: {department_name}")