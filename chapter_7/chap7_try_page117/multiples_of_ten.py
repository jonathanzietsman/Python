number = (input("Enter a number, and I'll tell you if it's a multiple of 10: "))

if int(number) % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")