# Initialize a loop that continues running until the user types 'quit'
while quit != 'quit':  
    # Prompt the user to enter a pizza topping
    quit = input("Enter a pizza topping: ")  
    
    # Display the topping being added to the pizza
    print("I will add " + quit + " to your pizza.")  
    
    # Check if the user entered 'quit' to stop the loop
    if quit == 'quit':  
        break  # Exit the loop if 'quit' is entered

# Display a thank you message after the loop ends
print("Thank you for ordering your pizza with us!")  
