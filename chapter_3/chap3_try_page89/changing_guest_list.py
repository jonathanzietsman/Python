# Original list of guests
guests = ["Albert Einstein", "Maya Angelou", "Nikola Tesla"]

# Print the original invitation messages
for guest in guests:
    print(f"Dear {guest}, I would be honored to invite you to dinner!")

# One guest can't make it
print("\nUnfortunately, Nikola Tesla can't make it to the dinner.")

# Replace the guest who can't make it with a new guest
guests[2] = "Marie Curie"

# Print a second set of invitation messages after the change
print("\nHere are the updated invitations:")
for guest in guests:
    print(f"Dear {guest}, I would be honored to invite you to dinner!")