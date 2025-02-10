def city_country(city, country, population=None):
    """Return a formatted string like 'Santiago, Chile' or 'Santiago, Chile – population 5000000'."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    return f"{city.title()}, {country.title()}"