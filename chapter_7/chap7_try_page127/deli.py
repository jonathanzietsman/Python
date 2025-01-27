# List called sandwich_orders
sandwich_orders = ["pastrami", "tuna", "beef", "chicken", "cream", "turkey"]

# Empty list called finished_sandwiches
finished_sandwiches = []

for name in sandwich_orders:
    print(f'I made your {name} sandwich.')
    finished_sandwiches.append(name)
    
print('\nMade sandwiches:')

for name in finished_sandwiches:
    print(f'I made a {name} sandwich.')