import pygame
from pygame.sprite import Sprite

class skeleton(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.guy = ai_game.guy
        self.angle = ai_game.angle
        self.screen_rect = ai_game.screen.get_rect()
        self.w, self.h = self.screen_rect.size

        self.skeleton = pygame.image.load('photos/skeleton_orange.png')
        self.orange_dead = pygame.image.load('photos/skeleton_orange_dead.png')
        self.blue_dead = pygame.image.load('photos/skeleton_blue_dead.png')
        self.white_dead = pygame.image.load('photos/skeleton_white_dead.png')
        self.black_dead = pygame.image.load('photos/skeleton_black_dead.png')
        self.yellow_dead = pygame.image.load('photos/skeleton_yellow_dead.png')

        self.rect = self.skeleton.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.px = ai_game.guy.x
        self.py = ai_game.guy.y

        self.orange_dead_rect = self.orange_dead.get_rect()
        self.blue_dead_rect = self.blue_dead.get_rect()
        self.black_dead_rect = self.black_dead.get_rect()
        self.white_dead_rect = self.white_dead.get_rect()
        self.yellow_dead_rect = self.yellow_dead.get_rect()

        self.orange_count = 0
        self.blue_count = 0
        self.black_count = 0
        self.white_count = 0
        self.yellow_count = 0

        self.skeleton_orange = True
        self.skeleton_blue = True
        self.skeleton_white = True
        self.skeleton_black = True
        self.skeleton_yellow = True

        self.color = 1

    def update_skeleton(self, ai_game):
        """Adaptive tracking so that the zombie moves towards the player at a constant speed."""

        self.px = ai_game.guy.x
        self.py = ai_game.guy.y

        if self.color == 1:
            self.x += self.settings.skeleton_speed * (self.px - self.x) * 0.001
            self.y += self.settings.skeleton_speed * (self.py - self.y) * 0.001
        elif self.color == 2:
            self.x += self.settings.skeleton_speed * (self.px - self.x) * 0.002
            self.y += self.settings.skeleton_speed * (self.py - self.y) * 0.002
        elif self.color == 3:
            self.x += self.settings.skeleton_speed * (self.px - self.x) * 0.003
            self.y += self.settings.skeleton_speed * (self.py - self.y) * 0.003
        elif self.color == 4:
            self.x += self.settings.skeleton_speed * (self.px - self.x) * 0.004
            self.y += self.settings.skeleton_speed * (self.py - self.y) * 0.004
        elif self.color == 5:
            self.x += self.settings.skeleton_speed * (self.px - self.x) * 0.005
            self.y += self.settings.skeleton_speed * (self.py - self.y) * 0.005

        self.rect.x = self.x
        self.rect.y = self.y

    def load_skeleton_orange(self):
        self.color = 1
        if self.skeleton_orange and self.orange_count <= 5:
            self.screen.blit(self.skeleton, (self.x, self.y))
        else:
            self.screen.blit(self.orange_dead, self.screen_rect.center)

    def load_skeleton_blue(self):
        self.color = 2
        self.skeleton = pygame.image.load('photos/skeleton_blue.png')
        if self.skeleton_blue and self.blue_count <= 10:
            self.screen.blit(self.skeleton, (self.x, self.y))
        else:
            self.screen.blit(self.blue_dead, self.screen_rect.center)

    def load_skeleton_black(self):
        self.color = 5
        self.skeleton = pygame.image.load('photos/skeleton_black.png')
        if self.skeleton_black and self.black_count <= 5:
            self.screen.blit(self.skeleton, (self.x, self.y))
        else:
            self.screen.blit(self.black_dead, self.screen_rect.center)

    def load_skeleton_white(self):
        self.color = 4
        self.skeleton = pygame.image.load('photos/skeleton_white.png')
        if self.skeleton_white and self.white_count <= 5:
            self.screen.blit(self.skeleton, (self.x, self.y))
        else:
            self.screen.blit(self.white_dead, self.screen_rect.center)

    def load_skeleton_yellow(self):
        self.color = 3
        self.skeleton = pygame.image.load('photos/skeleton_yellow.png')
        if self.skeleton_yellow and self.yellow_count <= 10:
            self.screen.blit(self.skeleton, (self.x, self.y))
        else:
            self.screen.blit(self.yellow_dead, self.screen_rect.center)

