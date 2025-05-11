from pathlib import Path
import json

# read data as a string and convert to a python object
path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\tutorial_2\Chapter 16\Mapping Global Datasets\eq_data\eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='UTF-8')
all_eq_data = json.loads(contents)

# examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    
print(mags[:10])
print(lons[:5])
print(lats[:5])



