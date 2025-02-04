""" Positional Arguments & Order Matters in Positional Arguments """
def create_account(username, password, email):
    print(f'\nAccount created for {username}.')
    print(f'Password: {password}')
    print(f'Email: {email}')
    
# correct order
create_account('john_doe', 'password123', 'john@example.com')

# incorrect order
create_account('john_doe', 'john@example.com', 'password123')




""" Keyword Arguments & Equivalent Function Calls """
def register_product(product_name, product_type, price):
    print(f'\nProduct: {product_name}')
    print(f'Type: {product_type}')
    print(f'Price: ${price}')
    
# using positional arguments
register_product('Laptop', 'Electronics', 999.99)

# using keyword arguments
register_product(product_name='Laptop', product_type='Electronics', price=999.99)

# changing the order with keyword arguments
register_product(product_name='Laptop', price=999.99, product_type='Electronics')

""" Default values and Equivalent function calls """
def sandwich(bread_type='whole wheat', filling='turkey'):
    print(f'\nBread: {bread_type} sandwich with {filling}')
    
# using default values
sandwich()

# providing custom values
sandwich(bread_type='white', filling='ham')

# using keyword arguments and changing the order
sandwich(filling='cheese', bread_type='whole wheat')




""" Avoiding arguments errors and multiple function calls """
def register_user(username, age, email):
    print(f'\nUser: {username}')
    print(f'Age: {age}')
    print(f'Email: {email}')
    
# correct function call
register_user('john_doe', 25, 'john@example.com')




""" Return values """
# define 3 parameters: first_name, last_name, and age (otional)
def build_person(first_name, last_name, age=None):
    # return a dictionary with persons information
    person = {'first': first_name, 'last': last_name}
    
    # if an age is provided, add it to the dict
    if age:
        person['age'] = age
        
    # return the dict
    return person




def greet_person():
    while True:
        # ask for first name, exit loop if user enters 'q'
        first_name = input('Enter your first name (or "q" to quit): ')
        if first_name.lower() == 'q':
            break
        
        # ask for last name, exit loop if user enters 'q'
        last_name = input('Enter your last name (or "q" to quit): ')
        if last_name.lower() == 'q':
            break
        
        # ask for age, make it optional 
        age = input('Enter your age (optional):')
        
        if age == '':
            age = None
        else:
            age = int(age)
            
        # call the build_person fuction
        person = build_person(first_name, last_name, age)
        
        # display the greeting with persons name
        print(f'\nHello, {person["first"]} {person["last"]}')
        
        # if age is provided, display it
        if 'age' in person:
            print(f'You are {person["age"]} years old')
            
# call the greet_person function to start the program
greet_person()




""" Passing a List """
# function to greet users
def greet_users(names):
    for name in names:
        print(f'Hello, {name}!')
        
# function to modify a list(moving designs from unprinted to completed)
def add_designs_to_completed(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_designs.append(current_design)
    
# function to prevent modification of the original list
def add_designs_to_completed_without_modifying_original(unprinted_designs, completed_designs):
    unprinted_designs_copy = unprinted_designs[:]
    
    while unprinted_designs_copy:
        current_design = unprinted_designs_copy.pop()
        completed_designs.append(current_design)
        
# Example 1: Passing a List to a function (greet_users)
usernames = ['alice', 'bob', 'charlie']
greet_users(usernames)

# Example 2: Modifying a list in a function
unprinted_designs = ['phone case', 'robot', 'pen holder']
completed_designs = []
add_designs_to_completed(unprinted_designs, completed_designs)

print('completed designs:', completed_designs)
print('unprinted designs:', unprinted_designs)

# Example 3: preventing a function from modifying the original list
unprinted_designs = ['phone case', 'robot', 'pen holder']
completed_designs = []

# works on a copy of the list 
add_designs_to_completed_without_modifying_original(unprinted_designs, completed_designs)
print('completed designs:', completed_designs)
print('unprinted designs:', unprinted_designs)




""" Passong a flexible number of arguments """
#passing an arbitrary number of arguments 
def make_pizza(*toppings):
    # print the list of toppings that have been ordered
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'onions', 'pineapple')




# mixing postional and arbitrary arguments
def make_pizza(size, *toppings):
    # summarize the pizza we making
    print(f'we are making a {size} pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')
        
make_pizza(16, 'pepperoni')
make_pizza(14, 'mushrooms', 'onions', 'pineapple')




# using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    # build a dictionary containing the user's profile information
    user_info['fist_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('jane', 'smith', location='new york', age=30)
print(user_profile)