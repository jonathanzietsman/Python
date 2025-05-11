# This program creates a visual representation of a random walk using matplotlib
# It demonstrates interactive plotting, color mapping, and user interaction

import matplotlib.pyplot as plt  # Import matplotlib for creating the visualization
from random_walk import RandomWalk  # Import our RandomWalk class

# Create and display random walks until the user chooses to stop
while True:
    # Create a new random walk with 50,000 points
    rw = RandomWalk(50_000)  # More points create a more interesting pattern
    rw.fill_walk()           # Generate the random walk data
    
    # Set up the plot with a classic style and large figure size
    plt.style.use('classic')  # Use a clean, professional plotting style
    fig, ax = plt.subplots(figsize=(15, 9))  # Create a large figure (15x9 inches)
    
    # Create a list of point numbers to use for coloring
    point_numbers = range(rw.num_points)
    
    # Plot the points with a color gradient based on their position in the walk
    ax.scatter(
        rw.x_values, rw.y_values,  # x and y coordinates
        c=point_numbers,           # Color points based on their order
        cmap=plt.cm.Blues,        # Use blue color gradient (darker = later points)
        edgecolors='none',        # Remove point outlines
        s=1                       # Small point size for clarity
    )
    ax.set_aspect('equal')  # Ensure the plot scales equally in both directions
    
    # Highlight the start and end points of the walk
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # Start point (green)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],           # End point (red)
              c='red', edgecolors='none', s=100)
    
    # Remove the axes for a cleaner look
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # Display the plot
    plt.show()
    
    # Ask if the user wants to generate another walk
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() != 'y':  # Exit if the answer isn't 'y' or 'Y'
        break