"""Create and update a mailing address using dictionaries."""

contact_info = {
    "name": "Patrick Green-Holloway",
    "address": "123 Main Street",
    "city": "Baltimore",
    "state": "Maryland",
    "zip": "21201",
}

mailing_address = (
    f"{contact_info['name']}\n"
    f"{contact_info['address']}\n"
    f"{contact_info['city']}, {contact_info['state']} {contact_info['zip']}"
)

print(mailing_address)

contact_info.pop("name")

full_name = {
    "first name": "Patrick",
    "last name": "Green-Holloway",
}

full_name.update({"honorific": "Mr."})

contact_info.update({"full_name": full_name})

updated_mailing_address = (
    f"{contact_info['full_name']['honorific']} "
    f"{contact_info['full_name']['first name']} "
    f"{contact_info['full_name']['last name']}\n"
    f"{contact_info['address']}\n"
    f"{contact_info['city']}, {contact_info['state']} {contact_info['zip']}"
)

print()
print(updated_mailing_address)