import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    # a class to manage the ship
    def __init__(self, ai_game):
        # initalize the ship and set its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # load the ships image and get its rect
        self.image = pygame.image.load(r'C:\01\Knowledge\Web Programming\codeCollage\Python\tutorial_1\ship.bmp')
        self.rect = self.image.get_rect()
        
        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)
        
        # movement flag: start with a ship thats not moving 
        self.moving_right = False
        self.moving_left = False
                
    def update(self):
        # update the ship's position based on the movement flag
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # Update rect object from self.x.
        self.rect.x = self.x
        
    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        # center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
        