cust_list = []


class RewardsProgram:
    '''A simple class that stores rewards customer information.'''

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f'Name: {self.cust_name}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')

    def thank_you(self):
        print(f'Thank you, {self.cust_name}, for visiting our restaurant!')

    def add_to_cust_list(self):
        customer = (self.cust_name, self.phone, self.email)
        cust_list.append(customer)


customer1 = RewardsProgram('Patrick Green-Holloway', '555-1000', 'patrick@example.com')
customer2 = RewardsProgram('Taylor Smith', '555-2000', 'taylor@example.com')
customer3 = RewardsProgram('Jordan Lee', '555-3000', 'jordan@example.com')

customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()

customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()

customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()

print(cust_list)
