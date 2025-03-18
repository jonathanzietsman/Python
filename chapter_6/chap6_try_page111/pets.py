# Define dictionaries for different pets
pets = [
    {
        "animal": "Dog",
        "owner": "Emily"
    },
    {
        "animal": "Cat",
        "owner": "Sarah"
    },
    {
        "animal": "Rabbit",
        "owner": "Jake"
    },
    {
        "animal": "Bird",
        "owner": "Lisa"
    },
    {
        "animal": "Fish",
        "owner": "Tom"
    },
    {
        "animal": "Hamster",
        "owner": "Rachel"
    },
    {
        "animal": "Turtle",
        "owner": "John"
    },
    {
        "animal": "Guinea Pig",
        "owner": "Olivia"
    },
    {
        "animal": "Horse",
        "owner": "Alex"
    },
    {
        "animal": "Snake",
        "owner": "David"
    }
]

# Loop through the list and print everything about each pet
for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print("-" * 20)
