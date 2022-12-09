import sys
import pygame
import math
from settings import Settings
from character import Guy
from bullet import Bullet
from doors import Doors
from items import Items
from skeletons import skeleton
import sound_effects as se
from Start import Start
import time
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
counter = 0


class Adventure:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.w, self.h = pygame.display.get_surface().get_size()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Adventure')
        self.angle = 90
        self.start = Start()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Medieval.ttf', 100)
        self.time_left = 90
        self.color = (255, 255, 255)

        self.guy = Guy(self)
            #Starting Screen Color
        self.bg_color = gray

        self.doors = Doors(self)
        self.items = Items(self)
        self.skeleton = skeleton(self)
        self.skeletons = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        se.backgroundsound.play(loops=-1)

    def run_game(self):
        # Nathan Smith helped create start button and start screen
        while True:
            if self.start.s == 0:
                self.start.run_start()
            elif self.start.s == 1:
                self._check_events()
                self._update_screen()
                self.guy.update()
                self.rotate_guy()
                self._update_bullets()
                # self.update_score()
            elif self.start.s == 2:
                self._check_events()
                self.guy.blitme()
                self.items.load_king()
                self.start.win_game()
                time.sleep(1)

    def _update_screen(self):
        if self.guy.rect.x == self.w:
            self.update_bgcolor_right()
        if self.guy.rect.x + self.guy.rect.width == 0:
            self.update_bgcolor_left()
        if self.guy.rect.y+self.guy.rect.height == 0:
            self.update_bgcolor_up()
        if self.guy.rect.y >= self.h:
            self.update_bgcolor_down()

        self.screen.fill(self.bg_color)

        if self.bg_color == gray:
            self.doors.make_door_gray()
            self.items.load_king()
            self._check_collision_gray()
        # elif self.bg_color == cyan:
        #     self.start.start_game()
        elif self.bg_color == white:
            self.doors.make_door_white()
            self.guy.white_key = False
            self.skeleton.load_skeleton_black()
            self.skeleton.update_skeleton(self)
            self._check_collision_white()
        elif self.bg_color == red:
            self.guy.red_key = False
            self.doors.make_door_red()
            self.skeleton.load_skeleton_orange()
            self.skeleton.update_skeleton(self)
            self._check_collision_red()
        elif self.bg_color == orange:
            self.doors.make_door_orange()
            self.guy.orange_key = False
        elif self.bg_color == yellow:
            self.guy.yellow_key = False
            self.doors.make_door_yellow()
            self.skeleton.load_skeleton_white()
            self.skeleton.update_skeleton(self)
            self._check_collision_yellow()
        elif self.bg_color == green:
            self.doors.make_door_green()
            self.skeleton.load_skeleton_blue()
            self.skeleton.update_skeleton(self)
            self._check_collision_green()
        elif self.bg_color == blue:
            self.doors.make_door_blue()
            self.guy.blue_key = False
        elif self.bg_color == purple:
            self.doors.make_door_purple()
            self.skeleton.load_skeleton_yellow()
            self.skeleton.update_skeleton(self)
            self._check_collision_purple()
        elif self.bg_color == pink:
            if not self.items.have_white:
                pygame.draw.rect(self.screen, black, pygame.Rect(0, self.h / 2 - 99, 30, 218))
            pygame.draw.rect(self.screen, white, pygame.Rect(0, self.h / 2 - 75, 20, 178))
            pygame.draw.rect(self.screen, purple, pygame.Rect(self.w - 20, self.h / 2 - 75, 20, 178))
        elif self.bg_color == black:
            self.doors.make_door_black()
            self.items.load_crown()
            self._check_collision_black()
            self.guy.black_key = False

        self.guy.blitme()


        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def update_bgcolor_up(self):
        if self.bg_color == blue:
            self.bg_color = purple
        elif self.bg_color == orange:
            self.bg_color = red

    def update_bgcolor_down(self):
        if self.bg_color == red:
            if self.items.have_orange:
                self.bg_color = orange
        elif self.bg_color == purple:
            self.bg_color = blue

    def update_bgcolor_right(self):
        if self.bg_color == gray:
            if self.items.have_red:
                self.bg_color = red
        elif self.bg_color == red:
            if self.items.have_blue:
                self.bg_color = blue
        elif self.bg_color == blue:
            if self.items.have_black:
                self.bg_color = black
        elif self.bg_color == cyan:
            self.bg_color = gray
        elif self.bg_color == green:
            self.bg_color = orange
        elif self.bg_color == orange:
            if self.items.have_yellow:
                self.bg_color = yellow
        elif self.bg_color == pink:
            self.bg_color = purple
        elif self.bg_color == white:
            self.bg_color = pink
        elif self.bg_color == black:
            self.bg_color = gray

    def update_bgcolor_left(self):
        if self.bg_color == red:
            self.bg_color = gray
        elif self.bg_color == blue:
            self.bg_color = red
        elif self.bg_color == orange:
            self.bg_color = green
        elif self.bg_color == yellow:
            self.bg_color = orange
        elif self.bg_color == purple:
            self.bg_color = pink
        elif self.bg_color == pink:
            if self.items.have_white:
                self.bg_color = white
        elif self.bg_color == cyan:
            self.bg_color = blue

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._fire_bullet()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.guy.moving_right = True
        elif event.key == pygame.K_a:
            self.guy.moving_left = True
        elif event.key == pygame.K_w:
            self.guy.moving_up = True
        elif event.key == pygame.K_s:
            self.guy.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        if self.start.win:
            if event.key == pygame.K_SPACE:
                self.start.s = 0

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.guy.moving_right = False
        elif event.key == pygame.K_a:
            self.guy.moving_left = False
        elif event.key == pygame.K_w:
            self.guy.moving_up = False
        elif event.key == pygame.K_s:
            self.guy.moving_down = False

    def mouse_angle(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.guy.rect.centerx, mouse_y - self.guy.rect.centery
        angle = (180/math.pi) * math.atan2(-rel_y, rel_x)
        return int(angle)

    def rotate_guy(self):
        self.angle = self.mouse_angle()
        self.guy.image = pygame.transform.rotate(self.guy.original_image, self.angle - 90)
        self.guy.rect = self.guy.image.get_rect(center=self.guy.rect.center)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            se.gunshot.play()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.centerx >= self.settings.screen_width or bullet.rect.centery < 0:
                self.bullets.remove(bullet)
            if bullet.rect.centery >= self.settings.screen_height or bullet.rect.centerx < 0:
                self.bullets.remove(bullet)
            if self.guy.rect.x >= self.settings.screen_width or self.guy.rect.right <= 0:
                self.bullets.remove(bullet)
            if self.guy.rect.y >= self.settings.screen_height or self.guy.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_collision_black(self):
        collision_crown = pygame.Rect.colliderect(self.guy.rect, self.items.crown_rect)
        if collision_crown:
            self.items.crowned = True
            self.guy.crowned = True

    def _check_collision_gray(self):
        collision_king = pygame.Rect.colliderect(self.guy.rect, self.items.king_sad_rect)
        collision_red_key = pygame.Rect.colliderect(self.guy.rect, self.items.red_key_rect)
        if collision_king:
            if self.guy.crowned:
                self.items.king_crowned = True
                self.guy.crowned = False
                self.start.s = 2
        if not self.items.have_red:
            self.items.load_red_key()
            if collision_red_key:
                self.guy.red_key = True
                self.items.have_red = True
                self.doors.red = False

    def _check_collision_green(self):
        self.skeletons.add(self.skeleton)
        collision_skeleton_bullet = pygame.sprite.groupcollide(self.bullets, self.skeletons, True, False)
        if collision_skeleton_bullet:
            self.skeleton.blue_count += 1
            self.items.blue_count += 1
        collision_blue_key = pygame.Rect.colliderect(self.guy.rect, self.items.blue_key_rect)
        if self.items.blue_count >= 11:
            if not self.items.have_blue:
                self.items.load_blue_key()
                if collision_blue_key:
                    self.guy.blue_key = True
                    self.items.have_blue = True
                    self.doors.blue = False

    def _check_collision_white(self):
        self.skeletons.add(self.skeleton)
        collision_skeleton_bullet = pygame.sprite.groupcollide(self.bullets, self.skeletons, True, False)
        if collision_skeleton_bullet:
            self.skeleton.black_count += 1
            self.items.black_count += 1
        collision_black_key = pygame.Rect.colliderect(self.guy.rect, self.items.black_key_rect)
        if self.items.black_count >= 6:
            if not self.items.have_black:
                self.items.load_black_key()
                if collision_black_key:
                    self.guy.black_key = True
                    self.items.have_black = True
                    self.doors.black = False

    def _check_collision_yellow(self):
        self.skeletons.add(self.skeleton)
        collision_skeleton_bullet = pygame.sprite.groupcollide(self.bullets, self.skeletons, True, False)
        if collision_skeleton_bullet:
            self.skeleton.white_count += 1
            self.items.white_count +=1
        collision_white_key = pygame.Rect.colliderect(self.guy.rect, self.items.white_key_rect)
        if self.items.white_count >= 6:
            if not self.items.have_white:
                self.items.load_white_key()
                if collision_white_key:
                    self.guy.white_key = True
                    self.items.have_white = True
                    self.doors.white = True

    def _check_collision_red(self):
        self.skeletons.add(self.skeleton)
        collision_skeleton_bullet = pygame.sprite.groupcollide(self.bullets, self.skeletons, True, False)
        collision_orange_key = pygame.Rect.colliderect(self.guy.rect, self.items.orange_key_rect)
        if collision_skeleton_bullet:
            self.skeleton.orange_count += 1
            self.items.orange_count +=1
        if self.items.orange_count >= 6:
            if not self.items.have_orange:
                self.items.load_orange_key()
                if collision_orange_key:
                    self.guy.orange_key = True
                    self.items.have_orange = True
                    self.doors.orange = False

    def _check_collision_purple(self):
        self.skeletons.add(self.skeleton)
        collision_skeleton_bullet = pygame.sprite.groupcollide(self.bullets, self.skeletons, True, False)
        collision_yellow_key = pygame.Rect.colliderect(self.guy.rect, self.items.yellow_key_rect)
        if collision_skeleton_bullet:
            self.skeleton.yellow_count += 1
            self.items.yellow_count +=1
        if self.items.yellow_count >= 11:
            if not self.items.have_yellow:
                self.items.load_yellow_key()
                if collision_yellow_key:
                    self.guy.yellow_key = True
                    self.items.have_yellow = True
                    self.doors.yellow = False

    def update_score(self):
        self.total_mins = self.time_left // 60  # minutes left
        self.total_sec = self.time_left - (60 * (self.total_mins))  # seconds left
        self.time_left -= 1
        if self.time_left > -1:
            self.text = self.font.render(("Time left: " + str(self.total_mins) + ":" + str(self.total_sec)), True,
                                         self.color)
            self.screen.blit(self.text, (200, 200))
            pygame.display.flip()
            pygame.event.wait(1000)  # making the time interval of the loop 1sec
        else:
            self.text = self.font.render("Time Over!!", True, self.color)
            self.screen.blit(self.text, (200, 200))
            pygame.display.flip()





if __name__ == '__main__':
    ai = Adventure()
    ai.run_game()
