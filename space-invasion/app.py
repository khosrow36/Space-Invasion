#!/usr/bin/env python3
import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    sett = Settings()
    pygame.init()
    screen = pygame.display.set_mode(
        (sett.width, sett.height))
    pygame.display.set_caption("Space Invasion")
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(sett.background)
        ship.draw_ship()
        pygame.display.flip()

run_game()