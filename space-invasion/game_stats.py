class GameStats():
    """Statistics fot the game"""

    def __init__(self, settings):
        self. settings = settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit