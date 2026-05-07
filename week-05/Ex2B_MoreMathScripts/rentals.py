import math

# Ask the user how many people are going on the tour
tourists = int(input("Enter the number of tourists: "))

# Known values
passengers_per_van = 15
cost_per_van = 250

# Calculate how many vans are needed
vans_needed = math.ceil(tourists / passengers_per_van)

# Calculate total van cost
total_cost = vans_needed * cost_per_van

# Calculate cost per person
cost_per_person = total_cost / tourists

# Display the results
print()
print("Tour Van Estimate")
print("-----------------")
print(f"{'Tourists:':<20}{tourists}")
print(f"{'Vans Needed:':<20}{vans_needed}")
print(f"{'Total Van Cost:':<20}${total_cost:.2f}")
print(f"{'Cost Per Person:':<20}${cost_per_person:.2f}")