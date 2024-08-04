from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path_death = Path('../weather_data/death_valley_2021_simple.csv')
path_sitka = Path('../weather_data/sitka_weather_2021_full.csv')
lines_death = path_death.read_text().splitlines()
lines_sitka = path_sitka.read_text().splitlines()

reader_death = csv.reader(lines_death)
reader_sitka = csv.reader(lines_sitka)
header_row_death = next(reader_death)
header_row_sitka = next(reader_sitka)

# Extract dates and high temperatures for Death Valley and Sitka.
dates_death, highs_death, lows_death = [], [], []
dates_sitka, highs_sitka, lows_sitka = [], [], []
for row_death, row_sitka in zip(reader_death, reader_sitka):
    current_date_death = datetime.strptime(row_death[2], '%Y-%m-%d')
    current_date_sitka = datetime.strptime(row_sitka[2], '%Y-%m-%d')
    try:
        high_death = int(row_death[3])
        low_death = int(row_death[4])
        high_sitka = int(row_sitka[7])
        low_sitka = int(row_sitka[8])
    except ValueError:
        print(f"Missing data for {current_date_death}")
    else:
        dates_death.append(current_date_death)
        highs_death.append(high_death)
        lows_death.append(low_death)
        dates_sitka.append(current_date_sitka)
        highs_sitka.append(high_sitka)
        lows_sitka.append(low_sitka)

# Plot the high and low temperatures for Death Valley and Sitka.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates_death, highs_death, color='red', alpha=0.5)
ax.plot(dates_death, lows_death, color='blue', alpha=0.5)
ax.fill_between(dates_death, highs_death, lows_death, color='gray', alpha=0.2)
ax.plot(dates_sitka, highs_sitka, color='red', alpha=0.5)
ax.plot(dates_sitka, lows_sitka, color='blue', alpha=0.5)
ax.fill_between(dates_sitka, highs_sitka, lows_sitka, color='green', alpha=0.2)

# Format the plots.
title = "Daily High and Low Temperatures, 2021\n  Sitka, AK and Death Valley, CA"
ax.set_title(title, fontsize=18)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate(rotation=0)
ax.set_ylabel('Temperature (°F)', fontsize=14)
ax.tick_params(labelsize=14)

plt.show()

