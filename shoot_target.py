import pygame
from settings import Settings
import game_functions as gf
from shooter import Shooter
from pygame.sprite import Group
from target import Target
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    target_settings = Settings()
    screen = pygame.display.set_mode((target_settings.screen_width, target_settings.screen_height))
    pygame.display.set_caption("Shoot The Box")

    play_button = Button(target_settings, screen, "Start")
    stats = GameStats(target_settings)
    sb = Scoreboard(target_settings, screen, stats)
    shooter = Shooter(target_settings, screen)
    target = Target(target_settings, screen)
    bullets = Group()
    while True:
        gf.check_events(target_settings, stats, screen, sb, shooter, target, bullets, play_button)
        if stats.game_active:
            shooter.update()
            gf.update_bullets(target_settings, stats, screen, sb, shooter, target, bullets)
            gf.update_target(target_settings, target)
        gf.update_screen(target_settings, stats, screen, sb, shooter, target, bullets, play_button)

run_game()
