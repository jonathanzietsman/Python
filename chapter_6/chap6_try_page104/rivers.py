rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Print each river and its country
print("Rivers and the countries they run through:")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Print each river
print("\nRivers:")
for river in rivers:
    print(f"  {river.title()}")

# Print each country
print("\nCountries:")
for country in rivers.values():
    print(f"  {country.title()}")
