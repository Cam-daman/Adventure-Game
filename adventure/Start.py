import pygame
from pygame.sprite import Sprite
from settings import Settings

gray = (150, 150, 150)
black = (0, 0, 0)
cyan = (0, 255, 255)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 150, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (200, 0, 255)
pink = (255, 0, 200)

class Start():
    def __init__(self):
        # self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.w, self.h = pygame.display.get_surface().get_size()
        self.base_font = pygame.font.Font('Medieval.ttf', 70)
        self.user_text1 = 'Find the crown and return it to the king!'
        self.user_text2 = 'Use mouse to aim and shoot! WASD to move'
        self.user_text3 = 'Press space to start!'
        self.win_text1 = 'You Win!!!'
        self.win_text2 = "Press 'Q' to quit"
        self.ded_txt = 'You Lose!!!'
        self.input_rect = pygame.Rect(self.w / 25, self.h / 3, 500, 110)
        self.color_active = blue
        self.color_passive = gray
        self.color = self.color_passive
        self.active = False
        self.win = False
        self.s = 0


    def run_start(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.s = 1
                    self.active = True
                else:
                    pygame.quit()
                    sys.exit()
        self.screen.fill(gray)
        if self.active:
            self.color = self.color_active
            self.s = 1
        else:
            self.color = self.color_passive

        text_surface1 = self.base_font.render(self.user_text1, True, black)
        self.screen.blit(text_surface1, (self.w/2 - 575, self.h/2-100))
        self.input_rect.w = max(100, text_surface1.get_width() + 10)

        text_surface2 = self.base_font.render(self.user_text2, True, black)
        self.screen.blit(text_surface2, (self.w/2 - 620, self.h/2 - 20))
        self.input_rect.w = max(100, text_surface2.get_width() + 10)

        text_surface3 = self.base_font.render(self.user_text3, True, black)
        self.screen.blit(text_surface3, (self.w/2 - 300, self.h/2 + 70))
        self.input_rect.w = max(100, text_surface3.get_width() + 10)
        pygame.display.flip()

    def win_game(self):
        self.win = True

        text_surface1 = self.base_font.render(self.win_text1, True, black)
        self.screen.blit(text_surface1, (self.w/2 - 600, self.h/2))
        self.input_rect.w = max(100, text_surface1.get_width() + 10)

        text_surface2 = self.base_font.render(self.win_text2, True, black)
        self.screen.blit(text_surface2, (self.w/2 - 600, self.h/2 + 100))
        self.input_rect.w = max(100, text_surface2.get_width() + 10)

        pygame.display.flip()
