# How do you convert a temperature from Fahrenheit to Celsius?

# Formula:
# Celsius = (Fahrenheit - 32) * 5 / 9

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")