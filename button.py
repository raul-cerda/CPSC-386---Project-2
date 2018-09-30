# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import pygame.font
import functions as func


class Button:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = 255, 255, 255
        self.font = pygame.font.SysFont(None, 48)
        self.font_title = pygame.font.SysFont(None, 150)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.centery = self.screen_rect.centery + 100

        self.msg_img, self.msg_img_rect = self.prep_msg(msg)

    # sets up play button text
    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, (0, 0, 0), self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center
        return self.msg_img, self.msg_img_rect

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)

    # draws play button, shows pong title, and hides screen elements to appear as menu
    def show_inactive_menu(self, first_time, winner):
        if first_time:
            title_img = self.font_title.render('PONG', True, (255, 255, 255), (0, 0, 0))
            title_img_rect = title_img.get_rect()
            title_img_rect.centerx = self.rect.centerx
            title_img_rect.centery = int(self.screen_rect.centery/2)

            sub_title_img = self.font_title.render('No Walls - (AI)', True, (50, 255, 50), (0, 0, 0))
            sub_title_rect = sub_title_img.get_rect()
            sub_title_rect.centerx = self.rect.centerx
            sub_title_rect.centery = title_img_rect.centery + 100

            self.screen.fill((0, 0, 0))
            self.screen.blit(title_img, title_img_rect)
            self.screen.blit(sub_title_img, sub_title_rect)
        else:
            self.screen.fill((0, 0, 0))
            func.show_winner(self.screen, winner)
        self.draw_button()
