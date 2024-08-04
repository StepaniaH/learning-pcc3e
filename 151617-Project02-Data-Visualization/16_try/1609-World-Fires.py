from pathlib import Path
import csv

import plotly.express as px

path = Path("./world_fires_1_day.csv")
reader = csv.reader(path.read_text().splitlines())
header_row = next(reader)

lats, lons, brighinesses = [], [], []
for row in reader:
    lats.append(float(row[0]))
    lons.append(float(row[1]))
    brighinesses.append(float(row[2]))

fig = px.scatter_geo(lat=lats, lon=lons, size = brighinesses,
                     color = brighinesses,
                     color_continuous_scale='Viridis',
                     labels={'color':'Brightness'},
                     projection="natural earth",
                     )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
