favorite_places = {
    "Emily": ["Paris", "New York", "Tokyo"],
    "Sarah": ["London", "Sydney"],
    "Jake": ["Amsterdam", "Barcelona", "Berlin"]
}

# Print each person's favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print("-" * 20)