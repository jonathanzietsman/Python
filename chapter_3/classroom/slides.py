# creating a list of car brands
car_brands = ["Toyota", "Honda", "Ford", "Chevrolet"]

# accessing the first element using index position 0
first_car = car_brands[0]

# using f-string to insert the list item into a string
message = (f"The first car brand in the list is {first_car.title()}.")

# printing the message
print(message)




# starting with a list of motorcycles
motorcycles = ["Honda", "Yamaha", "Suzuki"]

# modifying an element (change yamaha to ducati)
motorcycles[1] = "Ducati"
print(f'Modified list: {motorcycles}')

# adding an element to the end of the list using append()
motorcycles.append("Kawasaki")
print(f'Appended list: {motorcycles}')

#inserting an element at the beginning of the list using insert()
motorcycles.insert(0, "Harley-Davidson")
print(f'Inserted list: {motorcycles}')




# removing an element by index using del
del motorcycles[2]
print(f'Deleted list: {motorcycles}')

# using pop() to remove and return the last item
popped_motorcycle = motorcycles.pop()
print(f'Popped item: {popped_motorcycle}')
print(f'Popped list: {motorcycles}')

# removing an item by value using remove()
motorcycles.remove("ducati")
print(f'Removed list: {motorcycles}')

# final list
print(f'Final list: {motorcycles}')




# sample list
cars = ["Toyota", "Honda", "Ford", "Chevrolet"]

# sorting the list permanently 
cars.sort()
print(f'Sorted list: {cars}')

# sorting the list in reverse order 
cars.sort(reverse=True)
print(f'Reverse sorted list: {cars}')

# using sorted() to display the list temporarily sorted
original_list = ["Toyota", "Honda", "Ford", "Chevrolet"]
print("Original list: ", original_list)
print("Sorted list: ", sorted(original_list))

# showing that the original list remains unchanged
print("Original list: ", original_list)

# reversing the order of the list using reverse()
cars.reverse()
print(f'Reversed list: {cars}')

# finding the length of the list using len()
print(f'Length of the list: {len(cars)}')