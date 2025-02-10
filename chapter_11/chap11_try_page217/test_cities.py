# test_cities.py
import pytest
from city_country import city_country

def test_city_country():
    """Test that the function returns properly formatted city, country strings."""
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'










""" 

def city_country(city, country, population=None):
    if population:
        return f"{city.title()} / {country.title()} population {population}"  # wrong format
    return f"{city.title()} / {country.title()}"  # wrong format


"""