"""Create candy and fruit flavor combinations using tuples and a set."""

candy_types = ("Gummies", "Lollipops", "Taffy")
fruit_flavors = ("Strawberry", "Mango", "Watermelon")

candy_options = set()

candy_options.add(f"{fruit_flavors[0]} {candy_types[0]}")
candy_options.add(f"{fruit_flavors[1]} {candy_types[1]}")
candy_options.add(f"{fruit_flavors[2]} {candy_types[2]}")
candy_options.add(f"{fruit_flavors[1]} {candy_types[0]}")

print("Today's candy options include:")
print(candy_options)

print()

print("Today's candy options include:")
print(candy_options)

print()

print("Today's candy options include:")
print(candy_options)

# Order does not stay the same when running the code!