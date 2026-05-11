"""Calculate weekly gross pay and federal tax withholding."""

pay_rate = float(input("Enter your hourly pay rate: "))
hours_worked = float(input("Enter hours worked this week: "))
filing_status = input("Enter filing status, single or joint: ").lower()

regular_hours = 40
overtime_rate = pay_rate * 1.5
weeks_per_year = 52

if hours_worked > regular_hours:
    overtime_hours = hours_worked - regular_hours
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * overtime_rate
    weekly_gross_pay = regular_pay + overtime_pay
else:
    overtime_hours = 0
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0
    weekly_gross_pay = regular_pay

annual_gross_pay = weekly_gross_pay * weeks_per_year

if filing_status == "single":
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif annual_gross_pay < 25000:
        tax_rate = 0.10
    elif annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = 0.00
    elif annual_gross_pay < 25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

else:
    tax_rate = None

if tax_rate is None:
    print(f"Invalid filing status: {filing_status}")
else:
    weekly_tax_withheld = weekly_gross_pay * tax_rate
    weekly_net_pay = weekly_gross_pay - weekly_tax_withheld

    print()
    print("Weekly Pay and Tax Summary")
    print("--------------------------")
    print(f"You worked {hours_worked:.2f} hours this period.")
    print(f"Your filing status is {filing_status}.")
    print(f"Your weekly gross pay is ${weekly_gross_pay:.2f}.")
    print(f"Your estimated annual gross pay is ${annual_gross_pay:.2f}.")
    print(f"Your federal tax rate is {tax_rate:.0%}.")
    print(f"Your weekly federal tax withheld is ${weekly_tax_withheld:.2f}.")
    print(f"Your weekly net pay is ${weekly_net_pay:.2f}.")