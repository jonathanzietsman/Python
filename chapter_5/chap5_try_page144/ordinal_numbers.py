# list with numbers 1-9
numbers = range(1, 10)

# looping throught the list 
for number in numbers:
    # if elif else chain to determine ordinal number
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")