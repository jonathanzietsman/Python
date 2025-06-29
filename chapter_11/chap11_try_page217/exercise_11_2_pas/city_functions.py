""" 
! Modify function so it requires a third parameter, population. Santiago, Chile – population 5000000
! make 3rd parameter optional
! test_city_country() fails
"""

def city_country(city, country, population=None):
    """
    GPT COMMENT:
    This version makes the population parameter optional by setting its default to None.
    If population is provided, it adds it to the returned string.
    Otherwise, it returns just 'City, Country'.
    """
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
