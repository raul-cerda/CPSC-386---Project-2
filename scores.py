# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import pygame.font


class Scores:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 90)
        self.left_score = 0
        self.right_score = 0

        self.prep_scores()

    # prepare score numbers to be shown at top of screen
    def prep_scores(self):
        text_color = (40, 40, 40)
        self.left_score_img = self.font.render(str(self.left_score), True, text_color, (255, 255, 255))
        self.right_score_img = self.font.render(str(self.right_score), True, text_color, (255, 255, 255))

        self.left_score_rect = self.left_score_img.get_rect()
        self.right_score_rect = self.right_score_img.get_rect()

        self.left_score_rect.right = self.screen_rect.right/2 - 120
        self.left_score_rect.top = 30
        self.right_score_rect.left = self.screen_rect.right / 2 + 120
        self.right_score_rect.top = 30

    def show_scores(self):
        self.prep_scores()
        self.screen.blit(self.left_score_img, self.left_score_rect)
        self.screen.blit(self.right_score_img, self.right_score_rect)
