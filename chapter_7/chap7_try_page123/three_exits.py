""" # 1. Use a conditional test in the while statement to stop the loop
quit = ""
while quit != 'quit':
    quit = input("Enter a pizza topping: ")
    if quit != 'quit':
        print("I will add " + quit + " to your pizza.")
print("Thank you for ordering your pizza with us!")

# 2. Use an active variable to control how long the loop runs
active = True
while active:
    quit = input("Enter a pizza topping: ")
    if quit == 'quit':
        active = False
    else:
        print("I will add " + quit + " to your pizza.")
print("Thank you for ordering your pizza with us!")
 """
# 3. Use a break statement to exit the loop
while True:
    quit = input("Enter a pizza topping: ")
    if quit == 'quit':
        break
    print("I will add " + quit + " to your pizza.")
print("Thank you for ordering your pizza with us!")
