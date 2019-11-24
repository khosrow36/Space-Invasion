import sys
import pygame

def check_events():
    """Check keyboard/mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, ship):
    """Update the screen"""
    screen.fill(settings.background)
    ship.draw_ship()
    pygame.display.flip()