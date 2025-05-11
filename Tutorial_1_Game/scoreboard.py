import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """A class to report scoring information.
    Handles displaying the current score, high score, level, and remaining lives."""
    
    def __init__(self, ai_game):
        """Initialize scoreboard attributes.
        Args:
            ai_game: The main game instance containing game settings and statistics."""
        # Store references to game objects and settings
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Configure text appearance
        self.text_color = (30, 30, 30)  # Dark gray text
        self.font = pygame.font.SysFont(None, 48)  # Default system font, size 48
        
        # Prepare all score display elements
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        """Convert the current score into a rendered image.
        Rounds the score to the nearest 10 and adds commas for readability."""
        # Round score to nearest 10 and format with commas
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        # Create the score image
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        # Position the score in the top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """Convert the high score into a rendered image.
        Rounds the score to the nearest 10 and adds commas for readability."""
        # Round high score to nearest 10 and format with commas
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        # Create the high score image
        self.prep_high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        
        # Center the high score at the top of the screen
        self.high_score_rect = self.prep_high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        """Convert the current level into a rendered image."""
        # Create the level image
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        
        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        """Show how many ships (lives) the player has left.
        Creates a row of ship icons at the top left of the screen."""
        # Create a group to hold the ship icons
        self.ships = Group()
        # Create one ship icon for each life remaining
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            # Position each ship icon horizontally
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    
    def check_high_score(self):
        """Check if the current score is a new high score.
        Updates the high score display if a new high score is achieved."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def show_score(self):
        """Draw all scoring information to the screen.
        Displays the current score, high score, level, and remaining lives."""
        # Draw all score elements
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.prep_high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        
        