#!/usr/bin/env python3
import pygame
from settings import Settings
from ship import Ship
import game_functions as g_fun
from pygame.sprite import Group

def run_game():
    sett = Settings()
    pygame.init()
    screen = pygame.display.set_mode(
        (sett.width, sett.height))
    pygame.display.set_caption("Space Invasion")
    ship = Ship(screen, sett)
    bullets = Group()

    while True:
        g_fun.check_events(ship, sett, screen, bullets)
        ship.update_pos()
        bullets.update()
        g_fun.update_screen(sett, screen, ship, bullets)

run_game()