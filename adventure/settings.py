

class Settings:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 790

        self.guy_speed = 1
        self.guy_limit = 2

        self.enemy_speed = .5
        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        self.win = False

        # self.alien_speed = 1.0
        # self.fleet_drop_speed = 10
        # self.fleet_direction = 1
        #
        # self.speedup_scale = 1.1
        # # self.initialize_dynamic_settings()
        #
        # self.score_scale = 1.5

    # def initialize_dynamic_settings(self):
    #     self.guy_speed = 5
    #     self.bullet_speed = 3.0
    #     self.alien_speed = 1.0
    #     self.fleet_direction = 1
    #     self.alien_points = 50
    # def increase_speed(self):
    #     self.guy_speed *= self.speedup_scale
    #     self.bullet_speed *= self.speedup_scale
    #     self.alien_speed  *= self.speedup_scale
    #     self.alien_points = int(self.alien_points * self.score_scale)

