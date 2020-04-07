class Settings():
    """Game settings"""
    def __init__(self):
        #game settings
        self.width = 800
        self.height = 700
        self.background = (78, 120, 103)

        #ship settings
        self.ship_speed = 2

        #bullet settings
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 14
        self.bullet_color = 0, 0, 0

        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 #1: right, -1: left