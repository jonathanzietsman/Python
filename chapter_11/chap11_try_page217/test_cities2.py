import pytest
from city_functions import city_country

def test_city_country():
    """Test that the function returns properly formatted city, country strings."""
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

def test_city_country_population():
    """Test that the function includes population when provided."""
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile – population 5000000'







""" 

import pytest
from city_functions import city_country

def test_city_country():
    result = city_country('santiago', 'chile')
    assert result == 'Incorrect, Format'

def test_city_country_population():
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile – wrong population 5000000'


"""