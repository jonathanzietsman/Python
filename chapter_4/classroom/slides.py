# using range() function
for i in range(5):
    print(i)
    
# using range() with list()
even_numbers = list(range(0, 11, 2))
print(even_numbers)

# square root example (squares of numbers)
squares = []
for number in range (1, 4):
    square = number ** 2
    squares.append(square)
print(squares)

# using min(), max(), and sum()
numbers = [10, 20, 30, 40, 50]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# list comprehension
doubled_numbers = [number * 2 for number in range(1, 6)]
print(doubled_numbers)




# original list of fruits 
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# slicing a list: Get the first three fruits
sliced_fruits = fruits[:3]

# looping through a slice: print each fruit in the slice
print("The first three fruits are:")
for fruit in sliced_fruits:
    print(fruit.title())
    
# copying a list: make a copy of the entire list 
copied_fruits = fruits[:]

# modify the original list and show both lists
fruits.append('fig')
print("\nOriginal list of fruits:")
print(fruits)
print("\nCopied list of fruits:")
print(copied_fruits)




# defining a tuple
sizes = (200,50)

# looping through a tuple
print("Original sizes:")
for size in sizes:
    print(size)
    
# reassiging a new tuple (writing over the previous tuple)
sizes = (400,100)
print("New sizes:")
for size in sizes:
    print(size)
    