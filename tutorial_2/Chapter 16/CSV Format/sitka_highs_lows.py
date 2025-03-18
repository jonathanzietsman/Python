from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\tutorial_2\Chapter 16\CSV Format\weather_data\sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# extract and high temperatures 
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low =int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# plot the high and low temperatures
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
ax.set_title("Daily high and low temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)


plt.show()
