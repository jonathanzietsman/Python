# checking for equality
a = 10
b = 20
print(a == b)

# checking for inequality
print(a != b)

# using 'and' to check multiple conditions
x = 5
y = 10
print( x > 2 and y < 15)

# using 'or' to check multiple conditions
print(x < 2 or y > 5)

# checking whether a value is not in a list
numbers = [1, 2, 3, 4, 5]
print(6 not in numbers)

# boolean expressions
is_raining = False
has_umbrella = True
print(is_raining and has_umbrella)




# Ignoring case when checking for equality
str1 = "hello"
str2 = "HELLO"
print(str1.lower() == str2.lower())

# numerical comparisons
a = 25
b = 30
print(a < b)
print(a == b)
print(a >= b)

# using and to check multiple conditions
age = 18
is_student = True
print(age >= 18 and is_student)

# checking whether a value is in a list
colors = ["red", "blue", "green"]
print('Green' in colors)
print('yellow' in colors)




#1. example with multiple if statements
temperature = 30

if temperature > 25:
    print("It's hot outside!")
if temperature < 40:
    print("It's not freezing outside!")
if temperature == 30:
    print("It's 30 degrees outside!")

#2. example with if statements and if-else statements
color = 'blue'

if color == 'red':
    print("The color is red!")
else:
    print("The color is not red!")
    
#3. example with if statements and if-elif statements
grade = 87

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
    
    
    
    
# available items in store
available_items = ['milk', 'bread', 'eggs', 'flour', 'sugar']

# customer's shopping cart
shopping_cart = []

# asking the user to input items they want to add
item1 = input("Enter the first item you want to add: ")
item2 = input("Enter the second item you want to add: ")
item3 = input("Enter the third item you want to add: ")

# add items to shopping cart based on conditions 
if item1 in available_items:
    shopping_cart.append(item1)
    print(f"{item1} has been added to your shopping cart.")
else:
    print(f"{item1} is not available in the store.")
    
if item2 in available_items:
    shopping_cart.append(item2)
    print(f"{item2} has been added to your shopping cart.")
else:
    print(f"{item2} is not available in the store.")
    
if item3 in available_items:
    shopping_cart.append(item3)
    print(f"{item3} has been added to your shopping cart.")
else:
    print(f"{item3} is not available in the store.")
    
# checking for special items (e.g., discounts) before displaying the shopping cart
if 'milk' in shopping_cart:
    print("You have a 10% discount on milk!")
    
# display the shopping cart content
print("\nYour shopping cart contains:")
print(shopping_cart)

# no additional print statements for adding items to the purchase
if not shopping_cart:
    print("Your shopping cart is empty.")