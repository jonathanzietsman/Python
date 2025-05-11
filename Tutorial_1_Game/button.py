import pygame.font

class Button:
    """A class to create clickable buttons for the game.
    Handles button appearance, text rendering, and positioning."""
    
    def __init__(self, ai_game, msg):
        """Initialize button attributes.
        Args:
            ai_game: The main game instance containing the screen
            msg: The text to display on the button"""
        # Store references to the game screen
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set button dimensions and appearance
        self.width, self.height = 200, 50  # Button size in pixels
        self.button_color = (0, 135, 0)    # Green color for the button
        self.text_color = (255, 255, 255)  # White text
        self.font = pygame.font.SysFont(None, 48)  # Default system font, size 48
        
        # Create and center the button's rectangle
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # Prepare the button's text message
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Convert the message into a rendered image and center it on the button.
        Args:
            msg: The text to display on the button"""
        # Create the text image with the specified colors
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # Get the rectangle of the text image
        self.msg_image_rect = self.msg_image.get_rect()
        # Center the text on the button
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        """Draw the button and its message on the screen.
        First draws the button background, then overlays the text."""
        # Draw the button background
        self.screen.fill(self.button_color, self.rect)
        # Draw the button text
        self.screen.blit(self.msg_image, self.msg_image_rect)
            
        