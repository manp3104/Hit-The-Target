import sys
import pygame
from bullet import Bullet
from time import sleep

def check_keydown_events(target_settings, stats, screen, event, shooter, bullets):
    if event.key == pygame.K_q:
        update_high_score(stats)
        sys.exit()
    elif event.key == pygame.K_UP:
        shooter.moving_up = True
    elif event.key == pygame.K_DOWN:
        shooter.moving_down = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < target_settings.bullets_allowed:
            new_bullet = Bullet(target_settings, screen, shooter)
            bullets.add(new_bullet)

def update_high_score(stats):
    file = open("highest_score.txt", "w")
    file.write(str(stats.high_score))
    file.close()

def check_keyup_events(event, shooter):
    if event.key == pygame.K_UP:
        shooter.moving_up = False
    elif event.key == pygame.K_DOWN:
        shooter.moving_down = False

def check_events(target_settings, stats, screen, sb, shooter, target, bullets, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            update_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(target_settings, stats, screen, event, shooter, bullets)
            if event.key == pygame.K_p:
                start_game(target_settings, stats, sb, shooter, target)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, shooter)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(target_settings, stats, shooter, target, play_button, mouse_x, mouse_y)

def start_game(target_settings, stats, sb, shooter, target):
    target_settings.initialize_dynamic_settings()
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    sb.prep_score()
    sb.prep_high_score()
    stats.game_active = True
    target.center_target()
    shooter.center_shooter()

def check_play_button(target_settings, stats, shooter, target, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(target_settings, stats, sb, shooter, target)


def check_bullets_right(target_settings, stats, screen, shooter, target, bullets):
    screen_rect = screen.get_rect()
    for bullet in bullets.sprites():
        if bullet.rect.right >= screen_rect.right:
            bullets.empty()
            if stats.chances_left > 0:
                stats.chances_left -= 1
                target.center_target()
                shooter.center_shooter()
                sleep(1)
            else:
                stats.game_active = False
                pygame.mouse.set_visible(True)

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_bullet_target_collision(target_settings, stats, sb, target, bullets):
    collision = pygame.sprite.spritecollideany(target, bullets)
    if collision:
        bullets.empty()
        target_settings.increase_speed()
        stats.score += target_settings.score_points
        sb.prep_score()
        check_high_score(stats, sb)

def update_bullets(target_settings, stats, screen, sb, shooter, target, bullets):
    bullets.update()
    """
    for bullet in bullets.copy():
        if bullet.rect.right >= target_settings.screen_width:
            bullets.remove(bullet)
    """
    check_bullet_target_collision(target_settings, stats, sb, target, bullets)
    check_bullets_right(target_settings, stats, screen, shooter, target, bullets)

def update_target(target_settings, target):
    if target.check_edges():
        target_settings.target_direction *= -1
        target.update()
    else:
        target.update()

def update_screen(target_settings, stats, screen, sb, shooter, target, bullets, play_button):
    screen.fill(target_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    shooter.blitme()
    target.blitme()
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
