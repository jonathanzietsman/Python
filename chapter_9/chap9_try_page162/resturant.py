# Make a class called Restaurant
class Resturant:
    # The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    
    # Make a method called describe_restaurant() that prints these two pieces of information
    def describe_resturant(self):
        print(f'This Resturant is called {self.rest_name} and serves {self.food_type}')
    
    # Method called open_restaurant() that prints a message indicating that the restaurant is open.
    def open_resturant(self):
        print('This Resturant is Open')

# Make an instance called restaurant from your class
resturant = Resturant('Madjacks', 'Flapjacks')

# Print the two attributes individually, and then call both methods.
print(resturant.rest_name)
print(resturant.food_type)

resturant.describe_resturant()
resturant.open_resturant()