import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Single alien"""

    def __init__(self, screen, settings):
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