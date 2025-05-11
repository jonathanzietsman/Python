# This program creates a scatter plot of square numbers using matplotlib
# It demonstrates creating larger datasets, color mapping, and axis formatting

import matplotlib.pyplot as plt  # Import matplotlib's pyplot module for creating graphs

# Create a large dataset for a more detailed visualization
x_values = range(1, 1001)                    # Create 1000 x-values from 1 to 1000
y_values = [x ** 2 for x in x_values]        # Calculate square of each x-value using list comprehension

# Set the style of the plot to 'bmh' (a clean, professional style)
plt.style.use('bmh')

# Create a figure (the window) and axes (the actual plot)
fig, ax = plt.subplots()

# Create the scatter plot with several customizations:
# - c=y_values: Color points based on y-value
# - cmap=plt.cm.Blues: Use blue color gradient (darker blue for higher values)
# - s=10: Set point size to 10 (smaller points for cleaner look with large dataset)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Customize the plot with title and labels
ax.set_title("Square Numbers", fontsize=24)  # Add a title with large font
ax.set_xlabel("Value", fontsize=14)          # Label for x-axis
ax.set_ylabel("Square of Value", fontsize=14) # Label for y-axis

# Make the tick marks (numbers on axes) larger and easier to read
ax.tick_params(labelsize=14)

# Customize the range and format of the axes
ax.axis([0, 1100, 0, 1_100_000])            # Set x-range (0-1100) and y-range (0-1,100,000)
ax.ticklabel_format(style='plain')           # Display numbers normally (not in scientific notation)

# Display the plot in a new window
plt.show()