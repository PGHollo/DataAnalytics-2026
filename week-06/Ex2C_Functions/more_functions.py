def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(f'{city}, {state} {zip_code}')


def add_numbers(*numbers):
    total = 0
    equation = ''

    for number in numbers:
        total += number
        if equation == '':
            equation = str(number)
        else:
            equation += ' + ' + str(number)

    print(f'{equation} = {total}')


def display_receipt(total_due, amount_paid):
    print(f'Total Due: ${total_due:.2f}')
    print(f'Amount Paid: ${amount_paid:.2f}')

    if amount_paid >= total_due:
        change_due = amount_paid - total_due
        print(f'Change Due: ${change_due:.2f}')
    else:
        balance = total_due - amount_paid
        print(f'Remaining Balance: ${balance:.2f}')


display_mailing_label('Patrick Green-Holloway', '123 Data Ave', 'Baltimore', 'MD', '21201')
print()
display_mailing_label('Taylor Smith', '456 Python Rd', 'Columbia', 'MD', '21044')
print()

add_numbers(5)
add_numbers(5, 10)
add_numbers(5, 10, 15, 20)
print()

display_receipt(25, 30)
print()
display_receipt(25, 25)
print()
display_receipt(25, 20)
