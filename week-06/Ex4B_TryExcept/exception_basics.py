try:
    number = int('hello')
except ValueError:
    print('ValueError: That text cannot be converted to an integer.')
else:
    print(number)
finally:
    print("Let's try another one...")

try:
    m = banana
except NameError:
    print('NameError: The variable does not exist yet.')
else:
    print(m)
finally:
    print("Let's try another one...")

try:
    result = 'Sales: ' + 250
except TypeError:
    print('TypeError: A string and number cannot be added this way.')
else:
    print(result)
finally:
    print("Let's try another one...")

try:
    compile('if True print("missing colon")', '<string>', 'exec')
except SyntaxError:
    print('SyntaxError: The Python syntax is not valid.')
else:
    print('The syntax worked.')
finally:
    print("Let's try another one...")
