import pygame
import math
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.guy = ai_game.guy
        self.angle = 0 * ai_game.angle

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.centerx = ai_game.guy.rect.centerx
        self.rect.centery = ai_game.guy.rect.centery

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.distance_x = mouse_x - self.guy.rect.centerx
        self.distance_y = mouse_y - self.guy.rect.centery

        self.angle = math.atan2(self.distance_y, self.distance_x)

        self.x += self.settings.bullet_speed * (math.cos(self.angle))
        self.y += self.settings.bullet_speed * (math.sin(self.angle))

        self.rect.x = self.x
        self.rect.y = self.y


    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
