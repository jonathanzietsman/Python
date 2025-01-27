# Extended dictionary of cities with more details
cities = {
    "Paris": {
        "country": "France",
        "population": "2.2 million",
        "fact": "Paris is known as the City of Light.",
        "founded": "3rd century BC",
        "landmarks": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
        "avg_temperature": "12°C"
    },
    "New York": {
        "country": "United States",
        "population": "8.6 million",
        "fact": "New York City is home to the Statue of Liberty.",
        "founded": "1624",
        "landmarks": ["Empire State Building", "Central Park", "Times Square"],
        "avg_temperature": "13°C"
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Tokyo is famous for its bustling Shibuya Crossing.",
        "founded": "1603",
        "landmarks": ["Tokyo Tower", "Senso-ji Temple", "Shibuya Crossing"],
        "avg_temperature": "16°C"
    }
}

# Print each city's extended information
for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print(f"Founded: {info['founded']}")
    print(f"Famous Landmarks: {', '.join(info['landmarks'])}")
    print(f"Average Temperature: {info['avg_temperature']}")
    print("-" * 20)
