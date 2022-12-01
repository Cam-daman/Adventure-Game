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

    def load_crown(self):
        self.screen.blit(self.crown, (500,500))

    def load_sad_king(self):
        self.screen.blit(self.king_sad, self.screen_rect.center)

    # def load_enemy_1(self):