# Create a list of cities
cities = ["Tokyo", "Paris", "New York", "Cape Town", "Sydney"]

# Accessing Elements
print("Accessing elements in the list:")
print(f"The first city in the list is: {cities[0]}")
print(f"The last city in the list is: {cities[-1]}")

# Modifying Elements
print("\nModifying an element in the list:")
cities[1] = "Berlin"
print(f"Updated list: {cities}")

# Adding Elements
print("\nAdding elements to the list:")
cities.append("London")  # Add to the end
print(f"List after append: {cities}")
cities.insert(2, "Dubai")  # Add at index 2
print(f"List after insert: {cities}")

# Removing Elements
print("\nRemoving elements from the list:")
del cities[0]  # Remove the first element
print(f"List after del: {cities}")
removed_city = cities.pop()  # Remove the last element
print(f"List after pop: {cities}")
print(f"Removed city: {removed_city}")
cities.remove("Dubai")  # Remove by value
print(f"List after remove: {cities}")

# Organizing a List
print("\nOrganizing the list:")
print(f"Original list: {cities}")
print(f"List sorted temporarily: {sorted(cities)}")
print(f"List sorted temporarily in reverse: {sorted(cities, reverse=True)}")
cities.sort()  # Sort permanently
print(f"List after sort: {cities}")
cities.sort(reverse=True)  # Sort permanently in reverse
print(f"List after reverse sort: {cities}")
cities.reverse()  # Reverse the order
print(f"List after reverse: {cities}")

# Finding the Length of a List
print("\nFinding the length of the list:")
print(f"The number of cities in the list is: {len(cities)}")
