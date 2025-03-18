cities = {
    "Paris": {
        "country": "France",
        "population": "2.2 million",
        "fact": "Paris is known as the City of Light."
    },
    "New York": {
        "country": "United States",
        "population": "8.6 million",
        "fact": "New York City is home to the Statue of Liberty."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Tokyo is famous for its bustling Shibuya Crossing."
    }
}

# Print each city's information
for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print("-" * 20)
