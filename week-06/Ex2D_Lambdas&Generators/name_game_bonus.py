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
    clean_name = name.strip().title()
    short_name = trunc_name(name)

    yield f'{clean_name}, {clean_name}, bo-b{short_name}'
    yield f'banana fana fo-f{short_name}'
    yield f'me my mo-m{short_name}'
    yield f'{clean_name}!'


for test_name in ['Patrick', 'carly', 'CHARLIE', 'Aidan', 'Braden', 'Billy Bob']:
    for line in name_game(test_name):
        print(line)
    print()
