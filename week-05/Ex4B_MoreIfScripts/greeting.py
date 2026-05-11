"""Display a greeting based on the current hour."""

current_hour = int(input("Enter the current hour from 0 to 23: "))

if current_hour < 0 or current_hour > 23:
    print(f"Invalid hour: {current_hour}. Please enter a number from 0 to 23.")
elif current_hour >= 23 or current_hour < 4:
    print(f"What are you doing up so late??")
elif current_hour < 10:
    print(f"Good morning!")
elif current_hour < 17:
    print(f"Good day!")
else:
    print(f"Good evening!")