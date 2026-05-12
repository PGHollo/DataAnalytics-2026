
hours_worked = float(input("Enter the hours worked: "))
hourly_pay_rate = float(input("Enter the hourly pay rate: "))

gross_pay = hours_worked * hourly_pay_rate

print()
print("Gross Pay Summary")
print("-----------------")
print(f"{'Hours worked:':<20}{hours_worked:.2f}")
print(f"{'Hourly pay rate:':<20}${hourly_pay_rate:.2f}")
print(f"{'Gross pay:':<20}${gross_pay:.2f}")
