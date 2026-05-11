"""Calculate gross pay with overtime."""

pay_rate = float(input("Enter the hourly pay rate: "))
hours_worked = float(input("Enter the number of hours worked: "))

regular_hours = 40
overtime_rate = pay_rate * 1.5

if hours_worked > regular_hours:
    overtime_hours = hours_worked - regular_hours
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * overtime_rate
    gross_pay = regular_pay + overtime_pay
else:
    overtime_hours = 0
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0
    gross_pay = regular_pay

print()
print("Gross Pay Summary")
print("-----------------")
print(f"{'Pay Rate:':<20}${pay_rate:.2f}")
print(f"{'Hours Worked:':<20}{hours_worked:.2f}")
print(f"{'Regular Pay:':<20}${regular_pay:.2f}")
print(f"{'Overtime Hours:':<20}{overtime_hours:.2f}")
print(f"{'Overtime Pay:':<20}${overtime_pay:.2f}")
print(f"{'Gross Pay:':<20}${gross_pay:.2f}")