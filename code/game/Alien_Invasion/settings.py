''' setting holder '''


class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initalise the game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Ship setttings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3

    def isName(self):
        ''' this is the name return '''
        return "settings"

    def isValue(self):
        ''' this is the value return '''
        return "settings"
