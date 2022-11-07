class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1000
        self.screen_height = 400
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 20