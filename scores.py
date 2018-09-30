# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import pygame.font


class Scores:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 70)
        self.left_score = 0
        self.right_score = 0

        self.left_score_img, self.right_score_img, self.left_score_rect, self.right_score_rect = self.prep_scores()
        self.score_to_win_img, self.score_to_win_rect = self.prep_score_to_win()

    # prepare score numbers to be shown at top of screen
    def prep_scores(self):
        text_color = (40, 40, 40)
        self.left_score_img = self.font.render(str(self.left_score), True, text_color, None)
        self.right_score_img = self.font.render(str(self.right_score), True, text_color, None)

        self.left_score_rect = self.left_score_img.get_rect()
        self.right_score_rect = self.right_score_img.get_rect()

        self.left_score_rect.right = self.screen_rect.right/2 - 300
        self.left_score_rect.top = 50
        self.right_score_rect.left = self.screen_rect.right / 2 + 300
        self.right_score_rect.top = 50
        return self.left_score_img, self.right_score_img, self.left_score_rect, self.right_score_rect

    def prep_score_to_win(self):
        self.score_to_win_img = self.font.render('15 to Win', True, (80, 80, 80), None)
        self.score_to_win_rect = self.score_to_win_img.get_rect()
        self.score_to_win_rect.centerx = self.screen_rect.centerx
        self.score_to_win_rect.centery = 20
        return self.score_to_win_img, self.score_to_win_rect

    def show_scores(self):
        self.prep_scores()
        self.prep_score_to_win()
        self.screen.blit(self.score_to_win_img, self.score_to_win_rect)
        self.screen.blit(self.left_score_img, self.left_score_rect)
        self.screen.blit(self.right_score_img, self.right_score_rect)
