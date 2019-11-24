class Settings():
    """Game settings"""
    def __init__(self):
        #game settings
        self.width = 1400
        self.height = 1000
        self.background = (78, 120, 103)

        #ship settings
        self.ship_speed = 2

        #bullet settings
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 14
        self.bullet_color = 0, 0, 0