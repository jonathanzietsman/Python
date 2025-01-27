# Favorite languages dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# List of people who should take the poll
people_to_poll = ['jen', 'edward', 'michael', 'anna', 'phil']

# Loop through the list of people to check their poll status
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, you are invited to take the favorite languages poll!")
