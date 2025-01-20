# Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
pizza = ["Pepperoni", "Margherita", "BBQ Chicken"]

# 4-11: Copy list of pizzas and rename
friend_pizzas = pizza[:]

# 4-11: Add new pizza to the original list 
pizza.append("Meat Lover's")

# 4-11: Add new pizza to friend_pizzas
friend_pizzas.append("Veggie Lover's")

# 4-11: Prove you have two separate lists using a for loop to print both
print('My Favourite pizzas are: ')
for pizza in pizza:
    print(pizza)

print('\nMy friends favorite pizzas are: ')
for fpizza in friend_pizzas:
    print(fpizza)




""" for i in pizza:
    # Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
    print(f'I love {i} pizza!')

print('\nI really love pizza!')

 """