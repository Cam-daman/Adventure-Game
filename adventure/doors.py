import pygame
from pygame.sprite import Sprite


gray = (150, 150, 150)
cyan = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (237, 0, 0)
orange = (255, 150, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (200, 0, 255)
pink = (255, 0, 200)
gold = (255, 200, 20)

class Doors(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.guy = ai_game.guy
        self.angle = ai_game.angle
        self.screen_rect = ai_game.screen.get_rect()
        self.w, self.h = pygame.display.get_surface().get_size()

        self.orange = True
        self.red = True
        self.blue = True
        self.white = False
        self.black = True
        self.yellow = True

    def make_door_gray(self):
        if self.red:
            pygame.draw.rect(self.screen, black, pygame.Rect(self.w - 30, self.h / 2 - 99, 30, 198))
        pygame.draw.rect(self.screen, red, pygame.Rect(self.w-20, self.h/2-89, 20, 178))

    def make_door_red(self):
        pygame.draw.rect(self.screen, gray, pygame.Rect(0, self.h/2-75, 20, 178))
        if self.orange:
            pygame.draw.rect(self.screen, black, pygame.Rect(self.w / 2 - 109, self.h-30, 218, 40))
        if self.blue:
            pygame.draw.rect(self.screen, black, pygame.Rect(self.w - 30, self.h / 2 - 99, 30, 198))
        pygame.draw.rect(self.screen, blue, pygame.Rect(self.w - 20, self.h / 2 - 89, 20, 178))
        pygame.draw.rect(self.screen, orange, pygame.Rect(self.w/2-89, self.h-20, 178, 20))


    def make_door_orange(self):
        if self.yellow:
            pygame.draw.rect(self.screen, black, pygame.Rect(self.w - 30, self.h / 2 - 99, 30, 218))
        pygame.draw.rect(self.screen, yellow, pygame.Rect(self.w-20, self.h/2-75, 20, 178))
        pygame.draw.rect(self.screen, green, pygame.Rect(0, self.h/2 - 75, 20, 178))
        pygame.draw.rect(self.screen, red, pygame.Rect(self.w / 2 - 89, 0, 178, 20))

    def make_door_yellow(self):
        pygame.draw.rect(self.screen, orange, pygame.Rect(0, self.h / 2 - 75, 20, 178))

    def make_door_green(self):
        pygame.draw.rect(self.screen, orange, pygame.Rect(self.w-20, self.h/2-89, 20, 178))

    def make_door_blue(self):
        pygame.draw.rect(self.screen, purple, pygame.Rect(self.w / 2 - 89, 0, 178, 20))
        pygame.draw.rect(self.screen, red, pygame.Rect(0, self.h / 2 - 75, 20, 178))
        if black:
            pygame.draw.rect(self.screen, black, pygame.Rect(self.w - 30, self.h / 2 - 99, 30, 218))
        pygame.draw.rect(self.screen, black, pygame.Rect(self.w-20, self.h/2-75, 20, 178))

    def make_door_purple(self):
        pygame.draw.rect(self.screen, pink, pygame.Rect(0, self.h/2-75, 20, 178))
        pygame.draw.rect(self.screen, blue, pygame.Rect(self.w / 2 - 89, self.h - 20, 178, 20))

    def make_door_pink(self):
        pygame.draw.rect(self.screen, purple, pygame.Rect(self.w-20, self.h/2-75, 20, 178))
        if not white:
            pygame.draw.rect(self.screen, black, pygame.Rect(0, self.h / 2 - 99, 30, 218))
        pygame.draw.rect(self.screen, white, pygame.Rect(0, self.h / 2 - 75, 20, 178))

    def make_door_cyan(self):
        pygame.draw.rect(self.screen, blue, pygame.Rect(0, self.h / 2 - 75, 20, 178))
        pygame.draw.rect(self.screen, black, pygame.Rect(self.w-20, self.h / 2 - 75, 20, 178))

    def make_door_white(self):
        pygame.draw.rect(self.screen, pink, pygame.Rect(self.w-20, self.h/2-75, 20, 178))

    def make_door_black(self):
        pygame.draw.rect(self.screen, gold, pygame.Rect(self.w-20, self.h / 2 - 75, 20, 178))


