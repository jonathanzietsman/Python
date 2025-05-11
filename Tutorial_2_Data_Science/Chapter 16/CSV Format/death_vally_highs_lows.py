# This program reads Death Valley weather data and creates a temperature range plot
# It demonstrates error handling, data validation, and temperature visualization

from pathlib import Path    # For handling file paths
import csv                  # For reading CSV files
from datetime import datetime  # For parsing dates
import matplotlib.pyplot as plt  # For creating the visualization

# Set up the path to the Death Valley weather data file
path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\tutorial_2\Chapter 16\CSV Format\weather_data\death_valley_2021_simple.csv')

# Read the file and split it into lines
lines = path.read_text().splitlines()

# Create a CSV reader object to parse the data
reader = csv.reader(lines)
header_row = next(reader)  # Skip the header row (column names)

# Create empty lists to store the data we'll extract
dates, highs, lows = [], [], []  # Lists for dates, high temps, and low temps

# Process each row of data after the header
for row in reader:
    # Convert the date string (row[2]) to a datetime object
    current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Format: YYYY-MM-DD
    
    # Try to convert temperature strings to integers
    # Use try-except to handle missing or invalid data
    try:
        high = int(row[3])  # High temperature from column 4
        low = int(row[4])   # Low temperature from column 5
    except ValueError:
        # Skip dates with missing or invalid data
        print(f"Missing data for {current_date}")
    else:
        # Add valid data to our lists
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
# Create the temperature plot
plt.style.use('bmh')  # Use a clean, professional style
fig, ax = plt.subplots()

# Plot both high and low temperatures with transparency
ax.plot(dates, highs, color='red', alpha=0.5)   # High temps in semi-transparent red
ax.plot(dates, lows, color='blue', alpha=0.5)    # Low temps in semi-transparent blue

# Add a shaded region between high and low temperatures
ax.fill_between(dates, highs, lows,              # Fill between high and low lines
               facecolor='blue', alpha=0.1)      # Light blue shading

# Customize the plot with Death Valley-specific information
title = 'Daily high and low temperatures, 2021\nDeath Valley, CA'  # Two-line title
ax.set_title(title, fontsize=24)  # Add title with location
ax.set_xlabel('', fontsize=16)  # No x-label needed (dates are self-explanatory)
fig.autofmt_xdate()  # Rotate and align the x-axis labels for better readability
ax.set_ylabel("Temperature (F)", fontsize=16)  # Label y-axis
ax.tick_params(labelsize=16)  # Set font size for tick labels

# Display the plot
plt.show()