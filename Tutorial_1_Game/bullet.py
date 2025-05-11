import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the player's ship.
    Handles bullet creation, movement, and rendering on the screen."""
    
    def __init__(self, ai_game):
        """Initialize a bullet at the ship's current position.
        Args:
            ai_game: The main game instance containing game settings and resources."""
        super().__init__()
        # Store references to the game screen and settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rectangle at (0, 0) with the specified dimensions
        # Then position it at the top center of the ship
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's vertical position as a float for smooth movement
        self.y = float(self.rect.y)
        
    def update(self):
        """Update the bullet's position as it moves up the screen.
        The bullet moves at a constant speed defined in game settings."""
        # Move the bullet upward by subtracting the bullet speed
        self.y -= self.settings.bullet_speed
        # Update the bullet's rectangle position to match the float y value
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet on the screen using its color and rectangle."""
        pygame.draw.rect(self.screen, self.color, self.rect)