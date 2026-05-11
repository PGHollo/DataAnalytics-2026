"""Practice using a for loop with a list of positive words."""


def main():
    """Print a positive message for each word in the list."""
    great_words = [
        "amazing",
        "awesome",
        "excellent",
        "fantastic",
        "cool",
    ]

    for word in great_words:
        print(f"Loops are {word}!")

    print("I <3 loops")


main()