import pygame

class Ship():
    def __init__(self, screen):
        """Ship initialization"""
        self.screen = screen

        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def draw_ship(self):
        """Draws the ship"""
        self.screen.blit(self.image, self.rect)