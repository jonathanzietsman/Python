# This module defines a Die class for simulating a fair die with any number of sides
# It demonstrates class creation, initialization with default values, and random number generation

from random import randint  # Import randint to generate random numbers in a specific range

class Die:
    """A class representing a single die.
    
    This class simulates a fair die that can have any number of sides.
    It provides methods to create a die and roll it to get random values.
    
    Attributes:
        num_sides (int): The number of sides on the die
    """
    
    def __init__(self, num_sides=6):
        """Initialize a new die.
        
        Args:
            num_sides (int, optional): Number of sides on the die. Defaults to 6 for a standard die.
            
        The die will generate random numbers from 1 to num_sides when rolled.
        """
        self.num_sides = num_sides
        
    def roll(self):
        """Simulate rolling the die.
        
        Returns:
            int: A random value between 1 and the number of sides on the die,
                simulating a fair roll where each number has an equal chance.
        """
        return randint(1, self.num_sides)