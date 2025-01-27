favorite_numbers = {
    "Emily": [7, 21, 42],
    "Sarah": [3, 9, 15],
    "Jake": [8, 27, 56]
}

# Print each person's favorite numbers
for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
    print("-" * 20)
