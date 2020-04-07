#!/usr/bin/env python3
import pygame
from pygame.sprite import Group

from settings import Settings
from alien import Alien
from ship import Ship
import game_functions as g_fun
from game_stats import GameStats

def run_game():
    sett = Settings()
    pygame.init()
    screen = pygame.display.set_mode(
        (sett.width, sett.height))
    pygame.display.set_caption("Space Invasion")
    ship = Ship(screen, sett)
    bullets = Group()
    aliens = Group()
    g_fun.create_fleet(sett, screen, ship, aliens)
    stats = GameStats(sett)

    while True:
        g_fun.check_events(ship, sett, screen, bullets)

        if stats.game_active:
            ship.update_pos()
            g_fun.update_bullets(bullets, aliens, sett, screen, ship)
            g_fun.update_aliens(sett, stats, aliens, ship, screen, bullets)

        g_fun.update_screen(sett, screen, ship, aliens, bullets)

run_game()