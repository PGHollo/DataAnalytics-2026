# 1. Creating a string
text = "Python"

# 2. Indexing (positive and negative)
print("First character:", text[0])
print("Last character:", text[-1])

print ("First three characters:" , text[0:3])
print ("From index 2 to end:", text[2:])
print("Every second character:", text[ :: 2])

print("Characters in string:")
for char in text:
    print(char, end=" ")
print()

print ("Py in text?" , "Py" in text)
print("'Java' in text?", "Java" in text) # False

print("Length of string:", len(text)) # 6

print("Concatenation:", text + "3.11") # 'Python3.11'
# 'PythonPython'


print("Repetition:", text * 2)

# 8. Immutability demonstration
try:
    text [0] = "J" # This will raise an error
except TypeError as e:
    print("Strings are immutable:", e)

    print("range(5):")
for i in range(5):
    print(i, end=" ")
print()