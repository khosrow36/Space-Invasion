import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullets fired from the ship"""
    def __init__(self, settings, screen, ship):
        """Creates a bullet"""
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0,
            settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def update(self):
        """Moves the bullet"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)