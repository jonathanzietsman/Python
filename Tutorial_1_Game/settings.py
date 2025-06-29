class Settings:
    """A class to store all game settings for Alien Invasion.
    Manages both static settings that remain constant and dynamic settings that change during gameplay."""
    
    def __init__(self):
        """Initialize the game's static settings.
        These settings remain constant throughout the game session."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Light gray background
        
        # Ship Settings
        self.ship_speed = 5.5  # Horizontal movement speed
        self.ship_limit = 3    # Number of lives the player starts with
        
        # Bullet Settings
        self.bullet_speed = 20.0    # Vertical movement speed
        self.bullet_width = 3       # Width of bullet in pixels
        self.bullet_height = 15     # Height of bullet in pixels
        self.bullet_color = (60, 60, 60)  # Dark gray color
        self.bullets_allowed = 12   # Maximum number of bullets on screen
        
        # Alien Settings
        self.alien_speed = 2.0      # Horizontal movement speed #! ADJUSTED FOR DEMONSTRATION 2.0 
        self.fleet_drop_speed = 200.0 # Vertical drop speed when fleet changes direction #! ADJUSTED FOR DEMONSTRATION 3.0

        # Game Progression Settings
        self.speedup_scale = 1.1    # Factor by which game speeds up after each level
        self.score_scale = 1.5      # Factor by which alien point values increase
        
        # Initialize dynamic settings that change during gameplay
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game.
        These settings are reset when starting a new game."""
        # Movement speeds
        self.ship_speed = 5.5
        self.bullet_speed = 20.0
        self.alien_speed = 5.0
        
        # Fleet direction: 1 moves right, -1 moves left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50  # Points awarded for shooting an alien
        
    def increase_speed(self):
        """Increase game speed and point values after completing a level.
        This makes the game progressively more challenging and rewarding."""
        # Increase movement speeds
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        # Increase point values
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)  # Display new point value for debugging