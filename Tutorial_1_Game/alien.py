import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet.
    Handles alien appearance, movement, and screen boundary detection."""
    
    def __init__(self, ai_game):
        """Initialize an alien and set its starting position.
        Args:
            ai_game: The main game instance containing game settings and resources."""
        super().__init__()
        # Store references to the game screen and settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load the alien image and get its rectangular boundaries
        self.image = pygame.image.load(r'C:\Users\j8760\Desktop\Programming\CodeCollage\Python\Tutorial_1_Game\alien.bmp')
        self.rect = self.image.get_rect()
        
        # Position each new alien near the top left of the screen
        # This position will be adjusted when creating the fleet
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position as a float for smooth movement
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Check if the alien has reached either edge of the screen.
        Returns:
            bool: True if the alien is at the right or left edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Update the alien's position based on fleet direction and speed.
        The alien moves horizontally based on the fleet_direction setting."""
        # Move the alien horizontally based on speed and direction
        self.x += self.settings.alien_speed * self.settings.fleet_direction 
        # Update the alien's rectangle position to match the float x value
        self.rect.x = self.x