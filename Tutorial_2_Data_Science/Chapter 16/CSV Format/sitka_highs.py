# This program reads weather data from a CSV file and creates a temperature plot
# It demonstrates file handling, data parsing, and data visualization

from pathlib import Path    # For handling file paths
import csv                  # For reading CSV files
from datetime import datetime  # For parsing dates
import matplotlib.pyplot as plt  # For creating the visualization

# Set up the path to the weather data file
path = Path(r'C:\Users\j8760\Desktop\Programming\CodeCollage\Python\Tutorial_2_Data_Science\Chapter 16\CSV Format\weather_data\sitka_weather_07-2021_simple.csv')

# Read the file and split it into lines
lines = path.read_text().splitlines()

# Create a CSV reader object to parse the data
reader = csv.reader(lines)
header_row = next(reader)  # Skip the header row (column names)

# Create empty lists to store the data we'll extract
dates, highs = [], []  # Lists for dates and high temperatures

# Process each row of data after the header
for row in reader:
    # Convert the date string (row[2]) to a datetime object
    current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Format: YYYY-MM-DD
    
    # Convert the temperature string (row[4]) to an integer
    high = int(row[4])
    
    # Add the data to our lists
    dates.append(current_date)
    highs.append(high)
    
# Create the temperature plot
plt.style.use('classic')  # Use a clean, professional style
fig, ax = plt.subplots()  # Create a new figure and axes

# Plot the high temperatures in red
ax.plot(dates, highs, color='red')

# Customize the plot
ax.set_title("Daily High Temperatures, 2021", fontsize=24)  # Add title
ax.set_xlabel('', fontsize=16)  # No x-label needed (dates are self-explanatory)
fig.autofmt_xdate()  # Rotate and align the x-axis labels for better readability
ax.set_ylabel("Temperature (F)", fontsize=16)  # Label y-axis
ax.tick_params(labelsize=16)  # Set font size for tick labels

# Display the plot
plt.show()