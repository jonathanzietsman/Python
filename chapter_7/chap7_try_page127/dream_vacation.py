# Dictionary to store poll results
dream_vacations = {}

# Flag to keep the polling active
polling_active = True

while polling_active:
    # Ask for the user's name
    name = input("What is your name? ")
    
    # Ask about their dream vacation
    vacation = input("If you could visit one place in the world, where would you go? ")
    
    # Store the response in the dictionary
    dream_vacations[name] = vacation
    
    # Check if they want to let someone else respond
    repeat = input("Would you like to let another person respond? (yes/no) ").lower()
    if repeat == 'no':
        polling_active = False

# Polling is complete, print the results
print("\n--- Dream Vacation Poll Results ---")
for name, vacation in dream_vacations.items():
    print(f"{name.title()} would like to visit {vacation.title()}.")
