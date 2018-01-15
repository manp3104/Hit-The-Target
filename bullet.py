import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, target_settings, screen, shooter):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, target_settings.bullet_width, target_settings.bullet_height)
        self.rect.centery = shooter.rect.centery
        self.rect.right = shooter.rect.right

        self.x = float(self.rect.x)

        self.color = target_settings.bullet_color
        self.speed_factor = target_settings.bullet_speed

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
