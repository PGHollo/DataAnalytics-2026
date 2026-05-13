import random

print("randint(1, 10):", random.randint(1, 10))

print("random():", random.random())

fruits = ["apple", "banana", "cherry"]
print("choice(fruits):", random.choice(fruits))

# 4. random.choices(seq, k=n) > List of k random elements (with
print("choices(fruits, k=3):", random.choices(fruits, k=3))

# 5. random. sample(seq, k=n) + List of k unique random elements
print("sample(fruits, k=2):", random.sample(fruits, k=2))

# 6. random. shuffle(seq) + Shuffles a list in place
numbers = [1, 2, 3, 4, 5]
random. shuffle(numbers)
print("shuffled numbers:", numbers)