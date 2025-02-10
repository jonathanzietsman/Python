""" Exercise 9.1 """

# Make a class called Restaurant
class Restaurant:
    # The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    
    # Make a method called describe_restaurant() that prints these two pieces of information
    def describe_restaurant(self):
        print(f'This restaurant is called {self.rest_name} and serves {self.food_type}.')
    
    # Method called open_restaurant() that prints a message indicating that the restaurant is open.
    def open_restaurant(self):
        print('This restaurant is open.')

# Make an instance called restaurant from your class
restaurant = Restaurant('Madjacks', 'Flapjacks')

# Print the two attributes individually, and then call both methods.
print(restaurant.rest_name)
print(restaurant.food_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# Create IceCreamStand class inheriting from Restaurant
class IceCreamStand(Restaurant):
    # Add an attribute called flavors that stores a list of ice cream flavors
    def __init__(self, rest_name, food_type, flavours):
        super().__init__(rest_name, food_type)
        self.flavours = flavours
    
    # Make a method called show_flavours() that prints the list of flavors
    def show_flavours(self):
        print(f'This restaurant serves the following flavours: {", ".join(self.flavours)}')


# Create an instance of IceCreamStand
my_ice_cream_stand = IceCreamStand('Ice Delight', 'Ice Cream', ['Vanilla', 'Chocolate', 'Strawberry'])

# Call the methods
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.open_restaurant()
my_ice_cream_stand.show_flavours()
