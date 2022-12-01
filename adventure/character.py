import pygame
from pygame.sprite import Sprite

# from settings import Settings


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
        # self.bgcolor = ai_game.bgcolor

        self.screen_w, self.screen_h = self.screen_rect.size

        # res_image = pygame.transform.scale(self.image, (60, 48))
        # res_rect = res_image.get_rect(center=self.rect.center)
        # self.image = res_image
        # self.rect = res_rect
        self.rect.midleft = self.screen.get_rect().midleft

        # rot_image = pygame.transform.rotate(self.image, self.angle)
        # rot_rect = rot_image.get_rect(center=self.rect.center)
        # self.image = rot_image
        # self.rect = rot_rect

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
                    and (self.rect.y) >= (self.screen_h/2):
                self.moving_right = False
            else:
                self.moving_right = True
            self.x += self.settings.guy_speed

        if self.moving_left:
            if self.x <= self.screen_rect.left and self.rect.y <= (self.screen_h/2 - 130):
                self.moving_left = False
            elif self.x <= self.screen_rect.left and self.rect.y >= (self.screen_h/2):
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
        self.screen.blit(self.image, self.rect)



