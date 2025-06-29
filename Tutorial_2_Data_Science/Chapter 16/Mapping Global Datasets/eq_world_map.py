# Import the Path class to handle file paths.
from pathlib import Path

# Import the json module to parse JSON data.
import json

# Import Plotly Express, a library for creating interactive visualizations.
import plotly.express as px

# Create a Path object pointing to the 30-day earthquake GeoJSON file.
path = Path(r'C:\Users\j8760\Desktop\Programming\CodeCollage\Python\Tutorial_2_Data_Science\Chapter 16\Mapping Global Datasets\eq_data\eq_data_30_day_m1.geojson')

# Read the entire file contents as a UTF-8 encoded string.
contents = path.read_text(encoding='UTF-8')

# Parse the JSON string into a Python dictionary.
all_eq_data = json.loads(contents)

# Access the list of earthquake records in the 'features' key.
all_eq_dicts = all_eq_data['features']

# Create empty lists to store data: magnitudes, longitudes, latitudes, and earthquake titles.
mags, lons, lats, eq_titles = [], [], [], []

# Loop through each earthquake record to extract information.
for eq_dict in all_eq_dicts:
    # Extract the magnitude from the 'properties' dictionary.
    mag = eq_dict['properties']['mag']
    
    # Extract the longitude (x-coordinate) from the 'geometry' coordinates.
    lon = eq_dict['geometry']['coordinates'][0]
    
    # Extract the latitude (y-coordinate).
    lat = eq_dict['geometry']['coordinates'][1]
    
    # Extract the descriptive title of the earthquake (e.g., location and magnitude).
    eq_title = eq_dict['properties']['title']
    
    # Append each piece of data to the respective lists.
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

# Define the title of the visualization.
title = 'Global Earthquakes'

# Create an interactive scatter geo-plot:
# - lat and lon specify coordinates of each earthquake.
# - size of each marker represents magnitude.
# - color represents magnitude (continuous color scale).
# - labels define how the legend is displayed.
# - projection sets the type of world map.
# - hover_name shows the earthquake title when you hover over a point.
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale='Viridis',
    labels={'color': 'Magnitude'},
    projection='natural earth',
    hover_name=eq_titles
)

# Write the visualization to an HTML file so you can open it in a web browser.
fig.write_html('eq_wrld_map.html')
