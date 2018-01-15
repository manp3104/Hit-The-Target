import pygame

class Shooter():
    def __init__(self, target_settings, screen):
        self.screen = screen
        self.target_settings = target_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        self.center = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False

    def center_shooter(self):
        self.center = self.screen_rect.centery

    def update(self):
        if self.moving_up and self.rect.top >= 0:
            self.center -= self.target_settings.shooter_speed
        if self.moving_down and self.rect.bottom <= self.target_settings.screen_height:
            self.center += self.target_settings.shooter_speed
        self.rect.centery = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
