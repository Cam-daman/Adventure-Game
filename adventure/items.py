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
        self.orange_skeleton = pygame.image.load('photos/skeleton_orange.png')
        self.orange_skeleton_dead = pygame.image.load('photos/skeleton_orange_dead.png')
        self.orange_key = pygame.image.load('photos/orange_key.png')
        self.red_key = pygame.image.load('photos/red_key.png')

        self.king_sad_rect = self.king_sad.get_rect()
        self.king_happy_rect = self.king_happy.get_rect()
        self.crown_rect = self.crown.get_rect()
        self.orange_skeleton_dead_rect = self.orange_skeleton_dead.get_rect()
        self.orange_key_rect = self.orange_key.get_rect()
        self.red_key_rect = self.red_key.get_rect()
        self.skeleton_orange_rect = self.orange_skeleton.get_rect()

        self.skeleton_orange_rect.center = (self.w/2, self.h/2)
        self.crown_rect.center = (500, 500)
        self.king_sad_rect.center = (self.w/2, self.h/2)
        self.skeleton_orange_rect.center = (500, 500)
        self.orange_key_rect.center = (500, 700)
        self.red_key_rect.center = (500,500)

        self.crowned = False
        self.king_crowned = False
        self.have_orange = False
        self.have_red = False

        self.skeleton_orange = True
        self.key_red = False
        self.key_orange = False
        self.key_blue = False
        self.key_white = False

    def load_king(self):
        if self.king_crowned:
            self.screen.blit(self.king_happy, self.screen_rect.center)
        else:
            self.screen.blit(self.king_sad, self.screen_rect.center)

    def load_crown(self):
        if not self.crowned:
            self.screen.blit(self.crown, (500,500))

    def load_skeleton_orange(self):
        if self.skeleton_orange:
            self.screen.blit(self.orange_skeleton, self.screen_rect.center)
        else:
            self.screen.blit(self.orange_skeleton_dead, self.screen_rect.center)
            if not self.have_orange:
                self.screen.blit(self.orange_key, (500, 500))

    def load_key_red(self):
        if not self.have_red:
            self.screen.blit(self.red_key, (500, 500))



