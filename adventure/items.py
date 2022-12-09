import pygame
from pygame.sprite import Sprite

class Items(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.guy = ai_game.guy
        self.angle = ai_game.angle
        self.screen_rect = ai_game.screen.get_rect()

        self.w, self.h = self.screen_rect.size

        self.king_sad = pygame.image.load('photos/king_sad.png')
        self.king_happy = pygame.image.load('photos/king_happy.png')
        self.crown = pygame.image.load('photos/crown.png')


        self.king_sad_rect = self.king_sad.get_rect()
        self.king_happy_rect = self.king_happy.get_rect()
        self.crown_rect = self.crown.get_rect()


        self.crown_rect.center = (500, 500)
        self.king_sad_rect.center = (self.w / 2, self.h / 2)
            #KEYS
        self.orange_key = pygame.image.load('photos/orange_key.png')
        self.red_key = pygame.image.load('photos/red_key.png')
        self.blue_key = pygame.image.load('photos/blue_key.png')
        self.white_key = pygame.image.load('photos/white_key.png')
        self.black_key = pygame.image.load('photos/black_key.png')
        self.yellow_key = pygame.image.load('photos/yellow_key.png')

        self.orange_key_rect = self.orange_key.get_rect()
        self.red_key_rect = self.red_key.get_rect()
        self.blue_key_rect = self.blue_key.get_rect()
        self.white_key_rect = self.white_key.get_rect()
        self.black_key_rect = self.black_key.get_rect()
        self.yellow_key_rect = self.yellow_key.get_rect()

        self.orange_key_rect.center = (self.w/2, self.h/2)
        self.red_key_rect.center = (800, 200)
        self.blue_key_rect.center = (500, 700)
        self.white_key_rect.center = (800, 200)
        self.black_key_rect.center = (800, 200)
        self.yellow_key_rect.center = (800, 200)

        self.orange_count = 0
        self.blue_count = 0
        self.black_count = 0
        self.white_count = 0
        self.yellow_count = 0

        self.crowned = False
        self.king_crowned = False
        self.have_orange = False
        self.have_red = False
        self.have_orange = False
        self.have_blue = False
        self.have_white = False
        self.have_black = False
        self.have_yellow = False

    def load_king(self):
        if self.king_crowned:
            self.screen.blit(self.king_happy, self.screen_rect.center)
        else:
            self.screen.blit(self.king_sad, self.screen_rect.center)

    def load_crown(self):
        if not self.crowned:
            self.screen.blit(self.crown, (500,500))

    def load_orange_key(self):
        self.screen.blit(self.orange_key, (self.w/2, self.h/2))

    def load_red_key(self):
        self.screen.blit(self.red_key, (800, 200))

    def load_blue_key(self):
        self.screen.blit(self.blue_key, (500, 700))

    def load_white_key(self):
        self.screen.blit(self.white_key, (800, 200))

    def load_black_key(self):
        self.screen.blit(self.black_key, (800, 200))

    def load_yellow_key(self):
        self.screen.blit(self.yellow_key, (800, 200))







