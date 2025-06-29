# Import the Path class from the pathlib module.
# pathlib is used for handling filesystem paths in an object-oriented way.
from pathlib import Path

# Import the json module to work with JSON data.
import json

# Create a Path object pointing to the geojson file containing earthquake data.
# r'' is a raw string literal, so backslashes are not treated as escape characters.
path = Path(r'C:\Users\j8760\Desktop\Programming\CodeCollage\Python\Tutorial_2_Data_Science\Chapter 16\Mapping Global Datasets\eq_data\eq_data_1_day_m1.geojson')

# Read the entire contents of the file as a text string.
contents = path.read_text(encoding='UTF-8')

# Convert the JSON string into a Python dictionary.
all_eq_data = json.loads(contents)

# The GeoJSON file has a top-level key called 'features' that holds a list of all earthquake records.
all_eq_dicts = all_eq_data['features']

# Create empty lists to store magnitudes, longitudes, and latitudes.
mags, lons, lats = [], [], []

# Loop over each earthquake record (dictionary) in the list.
for eq_dict in all_eq_dicts:
    # Extract the magnitude of the earthquake from the 'properties' dictionary.
    mag = eq_dict['properties']['mag']
    
    # Extract the longitude and latitude from the 'coordinates' list in the 'geometry' dictionary.
    # coordinates format: [longitude, latitude, depth]
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    
    # Append the extracted values to the respective lists.
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Print the first 10 magnitudes to verify the data.
print(mags[:10])

# Print the first 5 longitudes to verify the data.
print(lons[:5])

# Print the first 5 latitudes to verify the data.
print(lats[:5])
