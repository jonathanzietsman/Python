# Creating dictionaries for each person
person_1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person_2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

person_3 = {
    'first_name': 'Emily',
    'last_name': 'Johnson',
    'age': 35,
    'city': 'Chicago'
}

# Storing all dictionaries in a list called 'people'
people = [person_1, person_2, person_3]

# Looping through the list and printing details about each person
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()  # For a blank line between each person's information
