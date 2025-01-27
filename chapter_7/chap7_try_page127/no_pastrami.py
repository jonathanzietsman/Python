# List called sandwich_orders
sandwich_orders = ["pastrami", "tuna", "pastrami", "chicken", "pastrami", "turkey"]

# Empty list called finished_sandwiches
finished_sandwiches = []

# deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.")

# while loop to remove all instances of pastrami from sandwich_orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

for name in sandwich_orders:
    print(f'I made your {name} sandwich.')
    finished_sandwiches.append(name)
    
print('\nMade sandwiches:')

for name in finished_sandwiches:
    print(f'I made a {name} sandwich.')