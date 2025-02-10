import random

# Create a list with 10 numbers and 5 letters
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 items from the list to create the winning ticket
winning_items = random.sample(items, 4)

# Define your ticket with 4 randomly selected items from the list
my_ticket = random.sample(items, 4)

# Initialize variables to track the number of attempts
attempts = 0

# Loop until your ticket matches the winning ticket
while my_ticket != winning_items:
    attempts += 1
    my_ticket = random.sample(items, 4)  # Generate a new random ticket

# Print how many attempts it took to win
print(f"It took {attempts} attempts to win with the ticket {my_ticket}.")
