# Ex2A_tips.py
# This program calculates the total due at a restaurant.

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results

# The str() function changes a number into text.
# We use str() here because Python cannot combine regular text with numbers unless the numbers are converted to strings.

# print("The total due is " + str(total_due))

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))

# print("Tip is " + str(tip))

print("Tip is " + format(tip, ".2f"))

print("Total due is " + str(total_due))