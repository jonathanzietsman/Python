import pytest
from city_functions import city_country

# Test simple city and country format.
def test_city_country():
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

# Test city, country, and population format.
def test_city_country_population():
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile – population 5000000'

