class Restaurant:
    '''A simple class that stores restaurant information.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')


restaurant1 = Restaurant('Crafty Crab', 'seafood')
restaurant2 = Restaurant('Noodle House', 'ramen')
restaurant3 = Restaurant('Taco Spot', 'tacos')

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()
