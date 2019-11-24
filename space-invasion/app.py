#!/usr/bin/env python3
import pygame
from settings import Settings
from ship import Ship
import game_functions as g_fun

def run_game():
    sett = Settings()
    pygame.init()
    screen = pygame.display.set_mode(
        (sett.width, sett.height))
    pygame.display.set_caption("Space Invasion")
    ship = Ship(screen)

    while True:
        g_fun.check_events()
        g_fun.update_screen(sett, screen, ship)

run_game()