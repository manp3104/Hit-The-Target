import pygame

class Target():
    def __init__(self, target_settings, screen):
        self.screen = screen
        self.target_settings = target_settings

        self.image = pygame.image.load('images/minus.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True

    def center_target(self):
        self.rect.y = self.screen_rect.centery

    def update(self):
        self.rect.y += self.target_settings.target_speed_factor*self.target_settings.target_direction

    def blitme(self):
        self.screen.blit(self.image, self.rect)
