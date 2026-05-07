import math

# Ask the user for the room dimensions
length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))

# Calculate the room area
area = length * width

# Each tile covers 1 square foot, so tiles needed equals area
tiles_needed = area

# Add 10% extra for chips, breakage, and mistakes
extra_tiles = tiles_needed * 0.10
total_tiles_needed = tiles_needed + extra_tiles

# Each box has 12 tiles
tiles_per_box = 12

# Calculate full boxes needed
boxes_needed = math.ceil(tiles_needed / tiles_per_box)
total_boxes_to_buy = math.ceil(total_tiles_needed / tiles_per_box)

# Display the results
print()
print("Tile Estimate")
print("-------------")
print(f"{'Room Area:':<25}{area:.2f} square feet")
print(f"{'Tiles Needed:':<25}{tiles_needed:.2f}")
print(f"{'Tiles with 10% Extra:':<25}{total_tiles_needed:.2f}")
print(f"{'Boxes Needed:':<25}{boxes_needed}")
print(f"{'Total Boxes to Buy:':<25}{total_boxes_to_buy}")