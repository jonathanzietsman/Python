# List of places to visit
locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']


print('Original list: ')
print(locations)

print('\nList in alphabetical order: ')
print(sorted(locations))

print('\nOriginal list after being sorted(): ')
print(sorted(locations))

print('\nList in reverse alphabetical order: ')
print(sorted(locations, reverse=True))

print('\nOriginal list after using sorted() with reverse=True: ')
print(locations)

print('\nChanging the order with reverse(): ')
locations.reverse()
print(locations)

print('\nList after using reverse() again to restore original order: ')
locations.reverse()
print(locations)

print('\nList after using sort() to arrange in alphabetical order: ')
locations.sort()
print(locations)

print('\nList after using sort() to arrange in reverse alphabetical order: ')
locations.sort(reverse=True)
print(locations)