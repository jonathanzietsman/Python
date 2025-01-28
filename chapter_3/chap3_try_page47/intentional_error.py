# List of cities
cities = ["Tokyo", "Paris", "New York", "Cape Town", "Sydney"]

# Intentionally causing an IndexError
print("Attempting to access an out-of-range index:")
try:
    print(cities[10])  # Index 10 does not exist
except IndexError as e:
    print(f"IndexError: {e}")

# Correcting the error
print("\nCorrecting the error by using a valid index:")
print(f"The last city in the list is: {cities[-1]}")
