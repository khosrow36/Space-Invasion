import sys
import pygame

def check_events(ship):
    """Check keyboard/mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship.moving_left = False

def update_screen(settings, screen, ship):
    """Update the screen"""
    screen.fill(settings.background)
    ship.draw_ship()
    pygame.display.flip()