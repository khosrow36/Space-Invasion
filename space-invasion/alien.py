import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Single alien"""

    def __init__(self, settings, screen):
        """Alien initialization"""
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('img/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def draw_alien(self):
        """Draw the alien"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return true if alien is at the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien"""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x