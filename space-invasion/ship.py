import pygame

class Ship():
    def __init__(self, screen, settings):
        """Ship initialization"""
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def update_pos(self):
        if self.moving_left:
            self.rect.centerx -= self.settings.ship_speed
        if self.moving_right:
            self.rect.centerx += self.settings.ship_speed

    def draw_ship(self):
        """Draws the ship"""
        self.screen.blit(self.image, self.rect)