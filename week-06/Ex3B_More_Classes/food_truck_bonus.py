class Restaurant:
    '''A simple parent class for restaurants.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')


class FoodTruck(Restaurant):
    '''A child class for a food truck.'''

    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)
        self.private_bookings = 'N'
        self.truck_location = ''
        self.location_history = []

    def accepts_private_bookings(self):
        answer = input('Does this food truck accept private bookings? Y/N ')
        self.private_bookings = answer.upper()

        if self.private_bookings == 'Y':
            print('This food truck currently accepts private bookings.')
        else:
            print('This food truck currently does not accept private bookings.')

    def relocate_truck(self):
        location = input("Enter the truck's current location: ")
        self.truck_location = location
        self.location_history.append(location)
        print(f'Truck is currently located at {self.truck_location}')


truck = FoodTruck('Rolling Tacos', 'tacos')
truck.describe_rest()

# I keep duplicate locations in the history because repeat visits can show popular spots.
# Uncomment the next lines to test the input prompts.
# truck.accepts_private_bookings()
# truck.relocate_truck()
# print(truck.location_history)
