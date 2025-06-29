# This program simulates rolling two dice and visualizes the results using plotly
# It demonstrates data collection, frequency analysis, and interactive visualization

import plotly.express as px  # Import plotly for creating interactive plots
from die import Die          # Import our Die class for dice simulation

# Create two six-sided dice (D6)
die_1 = Die()  # First die with default 6 sides
die_2 = Die()  # Second die with default 6 sides

# Simulate rolling both dice 1000 times
results = []  # List to store the sum of each roll
for roll in range(1000): #! ADJUSTED FOR DEMONSTRATION 1000
    result = die_1.roll() + die_2.roll()  # Roll both dice and add their values
    results.append(result)                 # Store the sum in our results list

# Analyze the results by calculating frequencies
frequencies = []  # List to store how many times each sum occurs
max_result = die_1.num_sides + die_2.num_sides  # Maximum possible sum (e.g., 6 + 6 = 12)
poss_results = range(2, max_result+1)           # Possible sums (2 to 12 for two D6)

# Count how many times each sum appears in the results
for value in poss_results:
    frequency = results.count(value)      # Count occurrences of each possible sum
    frequencies.append(frequency)         # Add the count to our frequencies list

# Create an interactive bar chart using plotly
title = "Results of rolling two D6 1000 times."
labels = {'x': 'Result', 'y': 'Frequency of Result'}  # Axis labels
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Customize the chart for better readability
fig.update_layout(xaxis_dtick=1)  # Show all integer values on x-axis

# Save the interactive chart as an HTML file
# This creates a webpage that shows the interactive visualization
fig.write_html('die_visual.html')