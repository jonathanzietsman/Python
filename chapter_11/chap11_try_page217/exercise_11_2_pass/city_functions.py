""" 
! Modify function population parameter is optional.
! test make sure test_city_country() passes
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
