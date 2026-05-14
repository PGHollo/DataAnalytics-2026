lambda arguments: expression
# contains any number of arguments but contains only one expression.

# Lambda function to double a number
doubler = lambda n: n * 2

print(doubler(5))

#

# Lambda function to add a number
add_numbers = lambda a, b: a + b

print(add_numbers(3, 7))

# Lambda function to determine largest number
largest = lambda x, y: x if x > y else y

print(largest(12, 8))


loan_amount = 250000
monthly_interest_rate = 0.05
years = 5
months = years * 12

calculate_payment = lambda principal, rate, num_months: (
    principal * rate * (1 + rate) ** num_months
) / ((1 + rate) ** num_months - 1)

monthly_payment = calculate_payment(
    loan_amount,
    monthly_interest_rate,
    months
)

print(f"Loan Amount: ${loan_amount:,.2f}")
print(f"Monthly Interest Rate: {monthly_interest_rate * 100:.2f}%")
print(f"Loan Term: {years} years")
print(f"Monthly Payment: ${monthly_payment:,.2f}")