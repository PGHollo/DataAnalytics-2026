"""Simple dice guessing game without using the random module."""

import time


def get_secret_roll():
    """Create a dice roll using the current time."""
    dice_sides = [1, 2, 3, 4, 5, 6]
    dice_pool = tuple(dice_sides)

    secret_index = int(time.time()) % len(dice_pool)

    return dice_pool[secret_index]


def main():
    """Run the dice guessing game."""
    dice_roll = get_secret_roll()
    guesses = []

    print("Dice Guessing Game")
    print("------------------")
    print("I rolled a dice.")
    print("Guess a number from 1 to 6.")

    while True:
        user_input = input("Enter your guess: ")

        if not user_input.isdigit():
            print("Please enter numbers only.")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 6:
            print("Please enter a number from 1 to 6.")
            continue

        guesses.append(guess)

        if guess < dice_roll:
            print("Higher")
        elif guess > dice_roll:
            print("Lower")
        else:
            print()
            print(f"Correct! The dice roll was {dice_roll}.")
            print(f"Number of guesses: {len(guesses)}")
            print(f"Your guesses: {guesses}")

            if len(guesses) < 5:
                print("You're awesome!")

            break


main()