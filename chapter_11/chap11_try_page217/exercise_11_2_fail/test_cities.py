from city_functions import city_country

def test_city_country():
    """
    GPT COMMENT:
    This test function checks that calling city_country() with only 'santiago' and 'chile'
    returns the formatted string 'Santiago, Chile'.
    However, at this step, the function requires a third argument, so this test will fail.
    """
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'
