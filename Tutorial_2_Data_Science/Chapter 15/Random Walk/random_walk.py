# This module defines a RandomWalk class to simulate random walk motion
# It demonstrates random number generation, step-by-step movement, and path tracking

from random import choice  # Import choice to randomly select from a list of values

class RandomWalk:
    """A class to generate random walks.
    
    This class simulates a random walk in 2D space, where each step
    is randomly chosen in terms of direction and distance. This can
    model various real-world phenomena like particle diffusion or
    animal movement patterns.
    
    Attributes:
        num_points (int): The number of points in the walk
        x_values (list): List of x-coordinates for each point
        y_values (list): List of y-coordinates for each point
    """
    
    def __init__(self, num_points=5000):
        """Initialize a random walk.
        
        Args:
            num_points (int, optional): Number of points in the walk. Defaults to 5000.
        """
        # Initialize attributes of the walk
        self.num_points = num_points
        
        # All walks start at the origin (0, 0)
        self.x_values = [0]  # List to store x-coordinates, starting at 0
        self.y_values = [0]  # List to store y-coordinates, starting at 0
        
    def fill_walk(self):
        """Generate the points in the random walk.
        
        This method calculates each point in the walk by:
        1. Randomly choosing a direction (positive or negative)
        2. Randomly choosing a distance (0-4 units)
        3. Combining direction and distance for both x and y
        4. Adding the new point to the walk
        
        The walk continues until reaching the specified number of points.
        Steps that would result in no movement are rejected.
        """
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far in the x-direction
            x_direction = choice([1, -1])                # Randomly choose right (1) or left (-1)
            x_distance = choice([0, 1, 2, 3, 4])        # Randomly choose how far to move
            x_step = x_direction * x_distance           # Calculate the total x movement
            
            # Decide which direction to go and how far in the y-direction
            y_direction = choice([1, -1])                # Randomly choose up (1) or down (-1)
            y_distance = choice([0, 1, 2, 3, 4])        # Randomly choose how far to move
            y_step = y_direction * y_distance           # Calculate the total y movement
            
            # Reject moves that go nowhere (when both steps are 0)
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the new position by adding the steps to the last position
            x = self.x_values[-1] + x_step              # Add x_step to last x-coordinate
            y = self.y_values[-1] + y_step              # Add y_step to last y-coordinate
            
            # Add the new position to our lists of points
            self.x_values.append(x)
            self.y_values.append(y)
            
    
    