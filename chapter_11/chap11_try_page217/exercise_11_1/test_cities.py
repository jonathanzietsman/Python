from city_functions import city_country

def test_city_country():
    """
    GPT COMMENT:
    This test function checks that calling city_country() with 'santiago' and 'chile'
    returns the correctly formatted string 'Santiago, Chile'.
    """
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'
