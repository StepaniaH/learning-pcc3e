from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path("./eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path("./eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquake in dataset.
all_eq_dicts = all_eq_data["features"]

mags, titls, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titls.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titls[:2])
print(lons[:5])
print(lats[:5])
