# Setting variable for age
age = 1000

# if person < 2 years old person = baby
if age < 2:
    print('This person is a baby.')

# if person >= 2 and < 4 years old person = toddler
elif age >= 2 and age < 4:
    print('This person is a toddler.')

# if person >= 4 and < 13 years old person = kid
elif age >= 4 and age < 13:
    print('This person is a kid.')

# if person >= 13 and < 20 years old person = teenager
elif age >= 13 and age < 20:
    print('This person is a teenager.')

# if person >= 20 and < 65 years old person = adult
elif age >= 20 and age < 65:
    print('This person is an adult.')

# if person >= 65 years old person = elder
elif age >= 65:
    print('This person is an elder.')
