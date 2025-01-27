while quit != 'quit':
    quit = input("Enter a pizza topping: ")
    print("I will add " + quit + " to your pizza.")
    if quit == 'quit':
        break
    
print("Thank you for ordering your pizza with us!")