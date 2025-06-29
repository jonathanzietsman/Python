from city_functions import city_country

def test_city_country_population():
    """
    GPT COMMENT:
    This test checks that calling city_country() with a population argument
    returns the correctly formatted string including the population.
    """
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile – population 5000000'
