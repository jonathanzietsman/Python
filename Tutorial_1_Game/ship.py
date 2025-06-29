import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the player's ship.
    Handles ship movement, positioning, and rendering on the screen."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position.
        Args:
            ai_game: The main game instance that contains all game settings and resources."""
        super().__init__()
        # Store references to the game screen and settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship's image and get its rectangular boundaries
        self.image = pygame.image.load(r'C:\Users\j8760\Desktop\Programming\CodeCollage\Python\Tutorial_1_Game\ship.bmp')
        self.rect = self.image.get_rect()
        
        # Position the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store the ship's exact horizontal position as a float for smooth movement
        self.x = float(self.rect.x)
        
        # Movement flags to track which direction the ship is moving
        self.moving_right = False
        self.moving_left = False
                
    def update(self):
        """Update the ship's position based on movement flags.
        Ensures the ship stays within the screen boundaries."""
        # Move the ship right if flag is set and ship isn't at screen edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # Move the ship left if flag is set and ship isn't at screen edge
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # Update the ship's rectangle position from the float x value
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the ship at its current position on the screen."""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Center the ship on the screen after a collision or game reset."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
        