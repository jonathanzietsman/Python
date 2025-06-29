""" 
! Modify function so it requires a third parameter, population. Santiago, Chile – population 5000000
! test_city_country() fails
"""

def city_country(city, country, population):
    """
    GPT COMMENT:
    This version of the function requires a third parameter: population.
    It returns a string formatted as 'City, Country – population xxx'.
    """
    return f"{city.title()}, {country.title()} - population {population}"
