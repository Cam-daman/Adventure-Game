import sys
import pygame
import math
from settings import Settings
from character import Guy
from bullet import Bullet
from doors import Doors
from items import Items
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
# from border import Border
# from map import Map
# from alien import Alien
# from time import sleep
# from stats import Scoreboard
# from button import Button
# from game_stats import GameStats


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

        # self.stats = GameStadts(self)
        # self.sb = Scoreboard(self)
        self.guy = Guy(self)
            #Starting Screen Color
        self.bg_color = red

        self.doors = Doors(self)
        # self.map = Map(self)
        self.bullets = pygame.sprite.Group()
        self.items = Items(self)
        self.skeletons = pygame.sprite.Group()


        # self.bgcolor = self.map.bgcolor
        # self.aliens = pygame.sprite.Group()
        # self._create_fleet()
        # self.play_button = Button(self, "Play")

    def run_game(self):
        while True:

            self._update_screen()
            self.guy.update()
            self._check_events()
            # if self.stats.game_active:
            self.rotate_guy()
            self._update_bullets()

            # self._update_aliens()

    def _update_screen(self):
        if self.guy.rect.x == self.w:
            self.update_bgcolor_right()
        if self.guy.rect.x + self.guy.rect.width == 0:
            self.update_bgcolor_left()
        if self.guy.rect.y+self.guy.rect.height == 0:
            self.update_bgcolor_up()
        if self.guy.rect.y == self.h:
            self.update_bgcolor_down()

        self.screen.fill(self.bg_color)

        if self.bg_color == gray:
            self.doors.make_door_gray()
            self.items.load_king()
            self.items.load_key_red()
            self._check_collision_gray()
        elif self.bg_color == cyan:
            self.doors.make_door_cyan()
        elif self.bg_color == white:
            self.doors.make_door_white()
        elif self.bg_color == red:
            self.items.have_red = False
            self.guy.red_key = False
            self.doors.red = False
            self.doors.make_door_red()
            self.items.load_skeleton_orange()
            self._check_collision_red()
        elif self.bg_color == orange:
            self.doors.make_door_orange()
            self.guy.orange_key = False
        elif self.bg_color == yellow:
            self.doors.make_door_yellow()
        elif self.bg_color == green:
            self.doors.make_door_green()
        elif self.bg_color == blue:
            self.doors.make_door_blue()
        elif self.bg_color == purple:
            self.doors.make_door_purple()
        elif self.bg_color == pink:
            self.doors.make_door_pink()
        elif self.bg_color == black:
            self.doors.make_door_black()
            self.items.load_crown()
            self._check_collision_black()

        self.guy.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # self.aliens.draw(self.screen)
        # self.sb.show_score()
        # if not self.stats.game_active:
        #     self.play_button.draw_button()
        pygame.display.flip()

    def update_bgcolor_up(self):
        if self.bg_color == gray:
            self.bg_color = gray
        elif self.bg_color == blue:
            self.bg_color = purple
        elif self.bg_color == orange:
            self.bg_color = red

    def update_bgcolor_down(self):
        if self.bg_color == red:
            if self.guy.orange_key:
                self.bg_color = orange
        elif self.bg_color == purple:
            self.bg_color = blue

    def update_bgcolor_right(self):
        if self.bg_color == gray:
            if self.guy.red_key:
                self.bg_color = red
        elif self.bg_color == red:
            self.bg_color = blue
        elif self.bg_color == blue:
            self.bg_color = cyan
        elif self.bg_color == cyan:
            self.bg_color = black
        elif self.bg_color == green:
            self.bg_color = orange
        elif self.bg_color == orange:
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
        elif self.bg_color == orange:
            self.bg_color = green
        elif self.bg_color == yellow:
            self.bg_color = orange
        elif self.bg_color == blue:
            self.bg_color = red
        elif self.bg_color == purple:
            self.bg_color = pink
        elif self.bg_color == pink:
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
                # mouse_pos = pygame.mouse.get_pos()
                # self._check_play_button(mouse_pos)

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
        if collision_red_key:
            self.guy.red_key = True
            self.items.have_red = True
            self.doors.red = True


    def _check_collision_red(self):
        self.skeletons.add(self.items.skeleton_orange_rect)
        collision_skeleton_bullet = pygame.sprite.groupcollide(self.bullets, self.skeletons, True, True)
        collision_orange_key = pygame.Rect.colliderect(self.guy.rect, self.items.orange_key_rect)
        if collision_skeleton_bullet:
            self.items.skeleton_orange = False
        if not self.items.skeleton_orange:
            if collision_orange_key:
                self.guy.orange_key = True
                self.items.have_orange = True
                self.doors.orange = True



    # def _create_fleet(self):
    #     alien = Alien(self)
    #     alien_width, alien_height = alien.rect.size
    #     available_space_x = self.settings.screen_width - (2 * alien_width)
    #     number_aliens_x = available_space_x // (2 * alien_width)
    #     guy_height = self.guy.rect.height
    #     available_space_y = (self.settings.screen_height - (3 * alien_height) - guy_height)
    #     number_rows = available_space_y // (2 * alien_height)
        #
        # for row_number in range(number_rows):
        #     for alien_number in range(number_aliens_x):
        #         self._create_alien(alien_number, row_number)

    # def _create_alien(self, alien_number, row_number):
    #     alien = Alien(self)
    #     alien_width, alien_height = alien.rect.size
    #     alien.x = alien_width + 2 * alien_width * alien_number
    #     alien.rect.x = alien.x
    #     alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    #     self.aliens.add(alien)

    # def _update_aliens(self):
    #     self._check_fleet_edges()
    #     self.aliens.update()
    #     if pygame.sprite.spritecollideany(self.guy, self.aliens):
    #         self._guy_hit()
    #     self._check_aliens_bottom()

    # def _check_fleet_edges(self):
    #     for alien in self.aliens.sprites():
    #         if alien.check_edges():
    #             self._change_fleet_direction()
    #             break
    # def _change_fleet_direction(self):
    #     for alien in self.aliens.sprites():
    #         alien.rect.y += self.settings.fleet_drop_speed
    #     self.settings.fleet_direction *= -1

    # def _check_play_button(self, mouse_pos):
    #     button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    #     if button_clicked and not self.stats.game_active:
    #         self.settings.initialize_dynamic_settings()
    #         self.stats.reset_stats()
    #         self.stats.game_active = True
    #         self.aliens.empty
    #         # self.bullets.empty()
    #         self._create_fleet()
    #         self.guy.center_guy()
    #         pygame.mouse.set_visible(False)
    #         self.sb.prep_score()
    #         self.sb.prep_level()
    #         self.sb.prep_guys()

    # def _guy_hit(self):
    #     if self.stats.guys_left > 0:
    #         self.stats.guys_left -= 1
    #         self.sb.prep_guys()
    #         self.aliens.empty()
    #         self.bullets.empty()
    #         self._create_fleet()
    #         self.guy.center_guy()
    #         sleep (0.5)
    #     else:
    #         self.stats.game_active = False
    #         pygame.mouse.set_visible(True)
    #

        # self._check_bullet_alien_collision()

    #     if not self.aliens:
    #         self.bullets.empty()
    #         self._create_fleet()
    #         self.settings.increase_speed()
    #         self.stats.level += 1
    #         self.sb.prep_level()

    # def _check_aliens_bottom(self):
    #     screen_rect = self.screen.get_rect()
    #     for alien in self.aliens.sprites():
    #         if alien.rect.bottom >= screen_rect.bottom:
    #             self._guy_hit()
    #             break

if __name__ == '__main__':
    ai = Adventure()
    ai.run_game()
