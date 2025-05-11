# This program creates a line plot of square numbers using matplotlib
# It demonstrates basic plotting, styling, and customization of graphs

import matplotlib.pyplot as plt  # Import matplotlib's pyplot module for creating graphs

# Create data for the plot
input_values = [1, 2, 3, 4, 5]  # X-axis values: numbers from 1 to 5
squares = [1, 4, 9, 16, 25]     # Y-axis values: squares of input_values

# Set the style of the plot to 'bmh' (a clean, professional style)
plt.style.use('bmh')

# Create a figure (the window) and axes (the actual plot)
fig, ax = plt.subplots()

# Create the line plot with input_values on x-axis and squares on y-axis
# linewidth=3 makes the line thicker and more visible
ax.plot(input_values, squares, linewidth=3)

# Customize the plot with title and labels
ax.set_title("Square Numbers", fontsize=24)  # Add a title with large font
ax.set_xlabel("Value", fontsize=14)          # Label for x-axis
ax.set_ylabel("Square of Value", fontsize=14) # Label for y-axis

# Make the tick marks (numbers on axes) larger and easier to read
ax.tick_params(axis='both', labelsize=14)

# Display the plot in a new window
plt.show()