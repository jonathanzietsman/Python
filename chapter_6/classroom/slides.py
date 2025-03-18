# person dictionary
person = {
    'name': 'Alice',
    'age': 30,
}

# looping through all key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
    
# looping through all keys
for key in person.keys():
    print(key)
    



# favourite colors dictionary
favorite_colors = {
    'Alice': 'blue',
    'Bob': 'green',
    'Charlie': 'red',
}

# looping through keys in a particular order (alphabetical order)
for key in sorted(favorite_colors.keys()):
    print(key)
    
# looping through all values in the dictionary
for color in favorite_colors.values():
    print(color)
    
# List of dictionaries, each representing a car's details
cars = [
    {'make': 'Toyota', 'model': 'Prius', 'year': 2015},
    {'make': 'Toyota', 'model': 'Corolla', 'year': 2013},
    {'make': 'Ford', 'model': 'Fiesta', 'year': 2016},
]

# loop through the list of dictionaries and print each car's details
for car in cars:
    print(f'car: {car["make"]} {car["model"]} ({car["year"]})')
    
# dictionary containing a list of colors
garage = {
    'colors': ['red', 'blue', 'green'],
    'location': 'home',
}

# accessing and printing the list of car colors in the dictionary
print(f'garage location: {garage["location"]}')
print('available colors:')
for color in garage['colors']:
    print(f'- {color}')
    
    
    
    
# define a dictionary
users = {
    'jdoe': {
        'first': 'john',
        'last': 'doe',
        'location': 'new york',
    },
    jsmith: {
        'first': 'jane',
        'last': 'smith',
        'location': 'san francisco',
    },
}

# looping through the outer dictionary to get user data
for username, user_data in users.items():
    print(f'username: {username}')
    
    # accessing and printing values from the inner dictionary
    full_name = f"{user_data['first']} {user_data['last']}"
    location = user_data['location']
    
    print(f'\tfull name: {full_name.title()}')
    print(f'\tlocation: {location.title()}')