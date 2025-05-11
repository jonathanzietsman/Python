class GameStats:
    """Track statistics for the Alien Invasion game.
    Manages player's score, lives, level, and high score."""
    
    def __init__(self, ai_game):
        """Initialize game statistics.
        Args:
            ai_game: The main game instance containing game settings."""
        # Store reference to game settings
        self.settings = ai_game.settings
        # Initialize game statistics
        self.reset_stats()
        
        # High score persists across game sessions
        self.high_score = 0
        
    def reset_stats(self):
        """Reset game statistics to their initial values.
        Called when starting a new game or when the player loses all lives."""
        # Set number of lives to the configured limit
        self.ships_left = self.settings.ship_limit
        # Reset score and level to starting values
        self.score = 0
        self.level = 1