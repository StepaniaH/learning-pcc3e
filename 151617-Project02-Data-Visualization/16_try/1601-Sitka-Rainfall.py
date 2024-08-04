from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('../weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, rainfalls = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rainfall = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainfalls.append(rainfall)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color='red', alpha=0.5)

title = "Daily Rainfall, 2021\nSitka, AK"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall (in)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
