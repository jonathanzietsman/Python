""" # asking for a number with a prompt
number = input("Enter a number: ")

# converting the input to an integer
number = int(number)

# checking if the number is even or odd using the modulo operator
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
     """



#1. moving item from one list to another 
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#2. removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print('/noriginal list:', pets)

while 'cat' in pets:
    pets.remove('cat')
    
print('updated list of pets:', pets)

#3. filling a dictionary with user input
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # store the response in the dictionary
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        polling_active = False
        
# show the results of the poll
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
    
    