import pygame.font
from pygame.sprite import Group
from character import Guy
import time

class Scoreboard:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Medieval.ttf', 100)

        self.time_left = 90  # duration of the timer in seconds
        self.crashed = False
        self.font = pygame.font.SysFont("Somic Sans MS", 30)
        self.color = (255, 255, 255)

    def update_score(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.crashed = True
        self.total_mins = self.time_left // 60  # minutes left
        self.total_sec = self.time_left - (60 * (self.total_mins))  # seconds left
        self.time_left -= 1
        if self.time_left > -1:
            self.text = self.font.render(("Time left: " + str(self.total_mins) + ":" + str(self.total_sec)), True, self.color)
            self.screen.blit(self.text, (200, 200))
            pygame.display.flip()
            self.screen.fill((20, 20, 20))
            time.sleep(1)  # making the time interval of the loop 1sec
        else:
            self.text = self.font.render("Time Over!!", True, self.color)
            self.screen.blit(text, (200, 200))
            pygame.display.flip()
    #     self.counter = 10
    #     self.text = self.font.render(str(self.counter), True, (0, 128, 0))
    #
    #     self.timer_event = pygame.USEREVENT + 1
    #     pygame.time.set_timer(self.timer_event, 1000)
    #
    # def update_score(self):
    #     self.clock.tick(60)
    #     for event in pygame.event.get():
    #         if event.type == self.timer_event:
    #             self.counter -= 1
    #             self.text = self.font.render(str(self.counter), True, (0, 128, 0))
    #             if self.counter == 0:
    #                 pygame.time.set_timer(self.timer_event, 0)
    #
    #     self.text_rect = self.text.get_rect(center=self.screen_rect.center)
    #     self.screen.blit(self.text, self.text_rect)
    #     pygame.display.flip()
    #
    # def prep_score(self):
    #     rounded_score = round(self.stats.score, -1)
    #     score_str = "{:,}".format(rounded_score)
    #     self.score_image = self.font.render(score_str,True,
    #             self.text_color, self.settings.bg_color)
    #     self.score_rect = self.score_image.get_rect()
    #     self.score_rect.right = self.screen_rect.right - 20
    #     self.score_rect.top = 20
    # def prep_high_score(self):
    #     high_score = round(self.stats.score, -1)
    #     high_score_str = "{:,}".format(high_score)
    #     self.high_score_image = self.font.render(high_score_str, True,
    #             self.text_color, self.settings.bg_color)
    #     self.high_score_rect = self.high_score_image.get_rect()
    #     self.high_score_rect.centerx = self.screen_rect.centerx
    #     self.high_score_rect.top = self.score_rect.top
    #
    # def prep_level(self):
    #     level_str = str(self.stats.level)
    #     self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
    #
    #     self.level_rect = self.level_image.get_rect()
    #     self.level_rect.right = self.score_rect.right
    #     self.level_rect.top = self.score_rect.bottom + 10
    #
    # def prep_ships(self):
    #     self.ships = Group()
    #     for ship_number in range(self.stats.ships_left):
    #         ship = Ship(self.ai_game)
    #         ship.rect.x = 10 + ship_number * ship.rect.width
    #         ship.rect.y = 10
    #         self.ships.add(ship)
    # def check_high_score(self):
    #     if self.stats.score > self.stats.high_score:
    #         self.stats.high_score = self.stats.score
    #         self.prep_high_score()
    # def show_score(self):
    #     self.screen.blit(self.score_image, self.score_rect)
    #     self.screen.blit(self.high_score_image, self.high_score_rect)
    #     self.screen.blit(self.level_image, self.level_rect)
    #     self.ships.draw(self.screen)
