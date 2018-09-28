# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import pygame.font


class Button:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = 255, 255, 255
        self.font = pygame.font.SysFont(None, 48)
        self.font_title = pygame.font.SysFont(None, 200)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    # sets up play button text
    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, (0, 0, 0), self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)

    # draws play button, shows pong title, and hides screen elements to appear as menu
    def show_inactive_menu(self):
        title_img = self.font_title.render('PONG', True, (255, 255, 255), (0, 0, 0))
        title_img_rect = title_img.get_rect()
        title_img_rect.centerx = self.rect.centerx
        title_img_rect.centery = int(self.screen_rect.centery/2)

        self.screen.fill((0, 0, 0))
        self.screen.blit(title_img, title_img_rect)
        self.draw_button()
