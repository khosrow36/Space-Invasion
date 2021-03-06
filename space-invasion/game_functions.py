import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ship, settings, screen, bullets):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            ship.moving_left = True
        if event.key == pygame.K_SPACE:
            fire_bullets(settings, screen, ship, bullets)

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

def fire_bullets(settings, screen, ship, bullets):
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)

def get_number_of_aliens_x(settings, alien_width):
    available_space_x = settings.width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_of_aliens_y(settings, ship_height, alien_height):
    available_space_y = (settings.height - (3 * alien_height) - ship_height)
    num_rows = int (available_space_y / (2 * alien_height))
    return num_rows

def create_fleet(settings, screen, ship, aliens):
    """Create aliens fleet"""
    alien = Alien(settings, screen)
    number_aliens_x = get_number_of_aliens_x(settings, alien.rect.width)
    number_aliens_y = get_number_of_aliens_y(settings, ship.rect.height, alien.rect.height)

    for row_num in range(number_aliens_y):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_num)

def update_screen(settings, screen, ship, aliens, bullets):
    """Update the screen"""
    screen.fill(settings.background)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.draw_ship()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets, aliens, settings, screen, ship):
    """Managing the bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    bullets_aliens_collisions(settings, screen, ship, aliens, bullets)

def bullets_aliens_collisions(settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def ship_hit(settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)

    else:
        stats.game_active = False

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(settings, stats, aliens, ship, screen, bullets):
    """Update the positions of aliens"""
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)