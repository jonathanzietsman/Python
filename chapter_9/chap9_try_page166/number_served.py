# Make a class called Restaurant
class Restaurant:
    # The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type
    # Add an attribute called number_served with a default value of 0
    def __init__(self, rest_name, food_type, number_served=0):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = number_served
    
    # Make a method called describe_restaurant() that prints these two pieces of information
    def describe_restaurant(self):
        print(f'This Restaurant is called {self.rest_name}, serves {self.food_type}, and has served {self.number_served} customers.')
    
    # Method called open_restaurant() that prints a message indicating that the restaurant is open.
    def open_restaurant(self):
        print('This Restaurant is Open')

    # Add a method called set_number_served() that lets you set the number of customers that have been served
    def set_number_served(self, number):
        self.number_served = number

    # Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
    def increment_number_served(self, number):
        self.number_served += number


# Create an instance called restaurant from this class
restaurant = Restaurant('Foodie Delight', 'Italian', 10)

# Print the number of customers the restaurant has served, and then change this value and print it again.
print(f'Number of customers served: {restaurant.number_served}')

# Changing attribute value and printing again 
restaurant.number_served = 20
print(f'Changed and updated number of customers served: {restaurant.number_served}')

# Call set_number_served method with a new number and print the value again.
restaurant.set_number_served(100)
print(f'Customers served after calling set_number_served method: {restaurant.number_served}')

# Increment number served and print again
restaurant.increment_number_served(50)
print(f'Customers served after calling increment_number_served method: {restaurant.number_served}')

# Call the methods to print the restaurant's name, cuisine type, and number of customers served
restaurant.describe_restaurant()
restaurant.open_restaurant()
