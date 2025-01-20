# Original list of guests
guests = ["Isaac Newton", "Albert Einstein", "Leonardo da Vinci", "Maya Angelou", "Nikola Tesla", "Charles Darwin"]

# Print the original invitation messages
print("I can only invite two people to dinner due to space constraints.\n")

# Remove guests one by one
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print a message for the two remaining guests
for guest in guests:
    print(f"\nDear {guest}, you’re still invited to dinner!")

# Remove the last two guests and print the empty list
del guests[:]
print("\nAfter removing the last two guests, the guest list is empty:")
print(guests)
