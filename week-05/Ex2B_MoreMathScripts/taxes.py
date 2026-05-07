# Federal taxes are 23% of your salary every month.
# This program calculates how much money is withheld for taxes.

salary = float(input("Enter your monthly salary: "))

tax_rate = 0.23

tax_withheld = salary * tax_rate

print(f"Federal tax withheld: ${tax_withheld:.2f}")