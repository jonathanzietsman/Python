# Ask user age
user_age = int(input("How old are you? "))

# If person is under 3, ticket is free
if user_age < 3:
    print("Your ticket is free.")
# If person is between 3 and 12, ticket is $10
elif user_age >= 3 and user_age <= 12:
    print("Your ticket is $10.")
# If person is over 12, ticket is $15
else:
    print("Your ticket is $15.")