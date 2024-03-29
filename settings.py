class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


        self.ships_limit = 3



        self.bullet_width = 30
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 30



        self.speedup_scale = 5
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        self.fleet_drop_speed = 10


    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 2.5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)