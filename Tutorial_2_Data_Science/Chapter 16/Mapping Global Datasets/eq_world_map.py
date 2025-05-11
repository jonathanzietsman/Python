from pathlib import Path
import json

import plotly.express as px

# read data as a string and convert to a python object
path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\tutorial_2\Chapter 16\Mapping Global Datasets\eq_data\eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='UTF-8')
all_eq_data = json.loads(contents)

# examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)
    
title = 'Gloabl Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags, color_continuous_scale='Viridis', labels={'color': 'Magnitude'}, projection='natural earth', hover_name=eq_titles)
fig.write_html('eq_wrld_map.html')
