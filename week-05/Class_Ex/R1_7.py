day_number = int(input("Enter a number from 1 through 7: "))

if day_number == 1:
    day = "Monday"
elif day_number == 2:
    day = "Tuesday"
elif day_number == 3:
    day = "Wednesday"
elif day_number == 4:
    day = "Thursday"
elif day_number == 5:
    day = "Friday"
elif day_number == 6:
    day = "Saturday"
elif day_number == 7:
    day = "Sunday"
else:
    day = "Invalid"

if day == "Invalid":
    print(f"Error: {day_number} is outside the range of 1-7.")
else:
    print(f"Day of the week: {day}")