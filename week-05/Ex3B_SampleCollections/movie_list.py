# Create a list of favorite movies
favorite_movies = [
    "Black Panther",
    "Creed",
    "The Dark Knight",
    "Spider-Man: No Way Home",
    "Remember the Titans"
]

# Print the length of the list and the complete list
print(
    f"The list favorite_movies includes my top "
    f"{len(favorite_movies)} favorite movies."
)
print(favorite_movies)

print()

# Use sorted() to print a sorted version of the list
print("Using sorted():")
print(sorted(favorite_movies))

# Print the original list again
print("Original list after sorted():")
print(favorite_movies)

# sorted() does not permanently change the original list.
# It only displays a sorted copy.

print()

# Use .sort() to permanently sort the list
print("Using .sort():")
favorite_movies.sort()
print(favorite_movies)

# .sort() permanently changes the original list order.

print()

# Add another movie to the list
favorite_movies.append("The Equalizer")

# Print the updated description and list
print(
    f"The list favorite_movies now includes my top "
    f"{len(favorite_movies)} favorite movies."
)
print(favorite_movies)