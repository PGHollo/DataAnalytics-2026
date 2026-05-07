# Ask the user for the temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Display the result using an f-string with 2 decimal places
print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")