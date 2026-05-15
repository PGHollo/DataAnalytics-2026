def get_valid_name(name):
    name = name.strip()

    if name == '':
        raise ValueError('Name cannot be blank.')
    if len(name) < 2:
        raise ValueError('Name must have at least two characters.')
    if name.isnumeric():
        raise ValueError('Name cannot be only numbers.')

    return name


def trunc_name(name):
    name = name.strip().lower()
    first_name = name.split()[0]

    if first_name[0] in 'aeiou':
        return first_name
    elif len(first_name) > 1 and first_name[1] not in 'aeiou':
        return first_name[2:]
    else:
        return first_name[1:]


def name_game(name):
    clean_name = get_valid_name(name).title()
    short_name = trunc_name(clean_name)

    yield f'{clean_name}, {clean_name}, bo-b{short_name}'
    yield f'banana fana fo-f{short_name}'
    yield f'me my mo-m{short_name}'
    yield f'{clean_name}!'


try:
    name_input = input('Enter a name: ')

    for line in name_game(name_input):
        print(line)
except ValueError as error:
    print(f'Invalid input: {error}')

# raise SystemExit(0) stops the full script with a successful exit code.
# It might be used instead of break when you want to stop the whole program.
# It can be unexpected because it exits everything, not just one loop.
