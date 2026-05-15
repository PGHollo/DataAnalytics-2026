class Restaurant:
    '''A restaurant class with customer counts and ratings.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')

    def add_num_served(self):
        customers = int(input('How many customers served today? '))
        self.number_served += customers

    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers')

    def customer_rating(self):
        rating = int(input('How would you rate your experience today on a scale of 1-5? '))

        while rating < 1 or rating > 5:
            print('Please enter a whole number from 1 to 5.')
            rating = int(input('How would you rate your experience today on a scale of 1-5? '))

        self.customer_ratings.append(rating)
        average = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f'Your rating was {rating}. The average rating for this restaurant is {average:.2f}')


restaurant1 = Restaurant('Crafty Crab', 'seafood')
restaurant1.print_num_served()

# The next lines use the methods with input prompts.
# Uncomment them when you want to test manually.
# restaurant1.add_num_served()
# restaurant1.print_num_served()
# restaurant1.customer_rating()
