import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ship, settings, screen, bullets):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            ship.moving_left = True
        if event.key == pygame.K_SPACE:
            new_bullet = Bullet(settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            ship.moving_left = False

def check_events(ship, settings, screen, bullets):
    """Check keyboard/mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship, bullets):
    """Update the screen"""
    screen.fill(settings.background)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.draw_ship()
    pygame.display.flip()