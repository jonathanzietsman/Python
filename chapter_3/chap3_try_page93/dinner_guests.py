# Exercise 3-6: More Guests
# Original list of guests
guests = ["Albert Einstein", "Maya Angelou", "Nikola Tesla"]

# Print the original invitation messages
for guest in guests:
    print(f"Dear {guest}, I would be honored to invite you to dinner!")

# Print message about the bigger dinner table
print("\nGreat news! I found a bigger dinner table, so I can invite more people.")

# Add new guests
guests.insert(0, "Isaac Newton")  # Add a guest at the beginning
guests.insert(2, "Leonardo da Vinci")  # Add a guest in the middle
guests.append("Charles Darwin")  # Add a guest at the end

# Print a new set of invitation messages after adding new guests
print("\nHere are the updated invitations:")
for guest in guests:
    print(f"Dear {guest}, I would be honored to invite you to dinner!")


# Exercise 3-9: Dinner Guests
print(f'\nThe Current Amount Of Guests Are: {len(guests)}')

