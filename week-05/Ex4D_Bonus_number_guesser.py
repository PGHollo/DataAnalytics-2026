"""Simple number guessing game without using the random module."""

import time

numbers = list(range(1, 21))
number_pool = tuple(numbers)

secret_index = int(time.time()) % len(number_pool)
secret_number = number_pool[secret_index]

guesses = []
guess_count = 0

print("Number Guessing Game")
print("--------------------")
print("I am thinking of a number from 1 to 20.")

while True:
    user_input = input("Enter your guess: ")

    if not user_input.isdigit():
        print("Please enter numbers only.")
        continue

    guess = int(user_input)
    guesses.append(guess)
    guess_count += 1

    if guess < secret_number:
        print("Higher")
    elif guess > secret_number:
        print("Lower")
    else:
        print(f"Correct! The number was {secret_number}.")
        print(f"Number of guesses: {guess_count}")
        print(f"Your guesses: {guesses}")

        if guess_count < 5:
            print("You're awesome!")

        break