""" 
! Function two parameters: city name, country name.
! return a single string of the form City, Country
! Test function make sure test_city_country() passes
"""
def city_country(city, country):
    """
    GPT COMMENT:
    This function accepts two parameters: city and country.
    It returns a formatted string of the form 'City, Country'.
    The .title() method capitalizes the first letter of each word.
    """
    return f"{city.title()}, {country.title()}"
