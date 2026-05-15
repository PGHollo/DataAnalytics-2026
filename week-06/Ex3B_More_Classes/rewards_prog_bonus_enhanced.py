cust_list = []


class RewardsProgram:
    '''A rewards customer with visit history and points.'''

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = 0

    def profile(self):
        print(f'Name: {self.cust_name}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')

    def thank_you(self):
        print(f'Thank you, {self.cust_name}, for visiting our restaurant!')

    def add_to_cust_list(self):
        customer = (self.cust_name, self.phone, self.email)
        cust_list.append(customer)

    def visit_rest(self):
        restaurant_name = input('Name of restaurant: ')
        food_bill = float(input('What was the total food bill for this visit? '))

        if restaurant_name not in self.restaurants_visited:
            self.restaurants_visited.append(restaurant_name)

        points = int(food_bill)
        self.rewards_points += points

        print(f'Points for this visit: {points}')
        print(f'Total rewards points earned: {self.rewards_points}')
        print(f'Thank you for visiting {restaurant_name}!')


customer1 = RewardsProgram('Patrick Green-Holloway', '555-1000', 'patrick@example.com')
customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()
print(cust_list)

# Uncomment the next line to test the visit prompt.
# customer1.visit_rest()
