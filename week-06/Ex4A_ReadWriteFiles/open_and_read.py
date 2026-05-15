f = open('about_me.txt', 'r')

first_50 = f.read(50)

next_four_lines = []
for i in range(1, 5):
    next_four_lines.append(f.readline())

next_100 = f.readlines(100)

f.close()

print(f'First 50 characters: {first_50}')
print(f'Next four lines, as list by line: {next_four_lines}')
print(f'Next 100 characters, as list by line, rounded up to complete lines: {next_100}')
