import pygame
from pygame.sprite import Sprite
from items import Items


class Guy(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.angle = ai_game.angle
        self.screen_rect = ai_game.screen.get_rect()

        self.original_image = pygame.image.load('photos/guy.bmp')
        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.screen_w, self.screen_h = self.screen_rect.size

        self.crowned = False
        self.orange_key = False
        self.red_key = False
        self.blue_key = False
        self.white_key = False
        self.black_key = False
        self.yellow_key = False

        self.rect.midleft = self.screen.get_rect().midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right:
            if (self.rect.width + self.x) >= self.screen_rect.right \
                    and self.rect.y <= (self.screen_h/2 - 130):
                self.moving_right = False
            elif (self.rect.width + self.x) >= self.screen_rect.right \
                    and self.rect.y >= (self.screen_h/2 + 20):
                self.moving_right = False
            else:
                self.moving_right = True
            self.x += self.settings.guy_speed

        if self.moving_left:
            if self.x <= self.screen_rect.left and self.rect.y <= (self.screen_h/2 - 130):
                self.moving_left = False
            elif self.x <= self.screen_rect.left and self.rect.y >= (self.screen_h/2 + 20):
                self.moving_left = False
            else:
                self.moving_left = True
            self.x -= self.settings.guy_speed

        if self.x > self.screen_rect.right:
            self.x = 0
        if self.rect.right < 0:
            self.x = self.screen_rect.right-self.rect.width

        self.rect.x = self.x

        if self.moving_up:
            if self.x < (self.screen_w/2 - 160) and self.y < self.screen_rect.top:
                self.moving_up = False
            elif self.x > (self.screen_w/2 + 10) and self.y < self.screen_rect.top:
                self.moving_up = False
            else:
                self.moving_up = True
            self.y -= self.settings.guy_speed

        if self.moving_down:
            if self.x < (self.screen_w/2 - 160) and self.y+self.rect.height > self.screen_h:
                self.moving_down = False
            elif self.x > (self.screen_w/2 + 10) and self.y+self.rect.height > self.screen_h:
                self.moving_down = False
            else:
                self.moving_down = True
            self.y += self.settings.guy_speed

        if self.rect.bottom < 0:
            self.y = self.screen_rect.bottom - self.rect.height
        if self.y > self.screen_rect.bottom:
            self.y = 0

        self.rect.y = self.y

    def blitme(self):
        if self.crowned:
            self.original_image = pygame.image.load('photos/guy_crowned.bmp')
            self.screen.blit(self.image, self.rect)
        elif self.orange_key:
            self.original_image = pygame.image.load('photos/guy_orange.png')
            self.screen.blit(self.image, self.rect)
        elif self.red_key:
            self.original_image = pygame.image.load('photos/guy_red.png')
            self.screen.blit(self.image, self.rect)
        elif self.blue_key:
            self.original_image = pygame.image.load('photos/guy_blue.png')
            self.screen.blit(self.image, self.rect)
        elif self.white_key:
            self.original_image = pygame.image.load('photos/guy_white.png')
            self.screen.blit(self.image, self.rect)
        elif self.black_key:
            self.original_image = pygame.image.load('photos/guy_black.png')
            self.screen.blit(self.image, self.rect)
        elif self.yellow_key:
            self.original_image = pygame.image.load('photos/guy_yellow.png')
            self.screen.blit(self.image, self.rect)
        else:
            self.original_image = pygame.image.load('photos/guy.bmp')
            self.screen.blit(self.image, self.rect)



