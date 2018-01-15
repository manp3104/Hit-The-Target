class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (109, 140, 170)

        # Bullet settings.
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 100, 100
        self.bullets_allowed = 1

        self.chances_allowed = 3
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.shooter_speed = 1
        self.bullet_speed = 2
        self.target_speed_factor = 1.5
        self.target_direction = 1
        self.score_points = 1

    def increase_speed(self):
        self.shooter_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed_factor *= self.speedup_scale
