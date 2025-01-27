car = 'subaru'  # Variable declaration

# True tests
print("Is car == 'subaru'? I predict True.")  # Test 1
print(car == 'subaru')  # True

print("\nIs car != 'audi'? I predict True.")  # Test 2
print(car != 'audi')  # True

print("\nIs car.lower() == 'subaru'? I predict True.")  # Test 3
print(car.lower() == 'subaru')  # True

print("\nIs len(car) == 6? I predict True.")  # Test 4
print(len(car) == 6)  # True (subaru has 6 letters)

print("\nDoes 'sub' in car? I predict True.")  # Test 5
print('sub' in car)  # True ('sub' is a substring of 'subaru')

# False tests
print("\nIs car == 'audi'? I predict False.")  # Test 6
print(car == 'audi')  # False

print("\nIs car != 'subaru'? I predict False.")  # Test 7
print(car != 'subaru')  # False

print("\nIs car.upper() == 'AUDI'? I predict False.")  # Test 8
print(car.upper() == 'AUDI')  # False (subaru != AUDI)

print("\nIs len(car) == 5? I predict False.")  # Test 9
print(len(car) == 5)  # False (subaru has 6 letters)

print("\nDoes 'toyota' in car? I predict False.")  # Test 10
print('toyota' in car)  # False ('toyota' is not a substring of 'subaru')


# Tests for equality and inequality with strings
fruit = "apple"
print(fruit == "apple")  # True
print(fruit != "banana")  # True
print(fruit == "orange")  # False
print(fruit != "apple")  # False

# Tests using the lower() method
greeting = "Hello"
print(greeting.lower() == "hello")  # True
print(greeting.lower() == "HELLO")  # False

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
number = 42
print(number == 42)  # True
print(number != 99)  # True
print(number > 10)   # True
print(number < 100)  # True
print(number >= 42)  # True
print(number <= 41)  # False

# Tests using the and keyword and the or keyword
age = 25
print(age > 18 and age < 30)  # True
print(age > 30 or age == 25)  # True
print(age > 30 and age == 25)  # False
print(age < 20 or age > 40)  # False

# Test whether an item is in a list
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
print("orange" in fruits)  # False

# Test whether an item is not in a list
print("grape" not in fruits)  # True
print("banana" not in fruits)  # False