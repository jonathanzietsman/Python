from city_functions import city_country

def test_city_country():
    """
    GPT COMMENT:
    This test checks that calling city_country() without a population argument
    returns the correctly formatted string excluding the population.
    """
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'