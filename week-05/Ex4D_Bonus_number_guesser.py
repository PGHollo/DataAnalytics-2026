import time

dice_sides = [1, 2, 3, 4, 5, 6]
dice_pool = tuple(dice_sides)

secret_index = int(time.time()) % len(dice_pool)
dice_roll = dice_pool[secret_index]

guesses = []
guess_count = 0

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
    guess_count += 1

    if guess < dice_roll:
        print("Higher")
    elif guess > dice_roll:
        print("Lower")
    else:
        print()
        print(f"Correct! The dice roll was {dice_roll}.")
        print(f"Number of guesses: {guess_count}")
        print(f"Your guesses: {guesses}")

        if guess_count < 5:
            print("You're awesome!")

        break