# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import pygame
import time
import pygame.mixer
from pygame.sprite import Sprite
import functions as func


class Ball(Sprite):

    def __init__(self, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.Surface((30, 30))
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.rect.centerx = self.screen_rect.right/2
        self.rect.top = self.screen_rect.bottom/2

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = (0, 0, 0)

        self.reverse_hori = 1
        self.reverse_vert = 1

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    # move ball around, bounce off objects, reset to mid screen when out of bounds
    # also stops game at 10 points
    def update_ball(self, ai_settings, paddles, score):
        if self.check_hori_edges(paddles, score):
            if score.left_score < 10 and score.right_score < 10:
                self.reset_ball()
                time.sleep(0.65)
            else:
                ai_settings.game_active = False
                func.reset_game(score, self, paddles, self.screen)
        self.check_vert_edges()

        self.x += self.reverse_hori
        self.y += self.reverse_vert

        self.rect.x = self.x
        self.rect.y = self.y

    # ball checks if out of bounds or about to bounce off paddle, out of bounds = point increase
    def check_hori_edges(self, paddles, score):
        if self.rect.right >= self.screen_rect.right:
            ping = pygame.mixer.Sound('sounds\scored.wav')
            ping.play()
            score.left_score += 1
            return True
        if self.rect.left <= 0:
            ping = pygame.mixer.Sound('sounds\scored.wav')
            ping.play()
            score.right_score += 1
            return True
        if pygame.sprite.spritecollideany(self, paddles):
            ping = pygame.mixer.Sound('sounds\ping.wav')
            ping.play()
            self.reverse_hori *= -1
        return False

    # bounces off top and bottom of screen
    def check_vert_edges(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            self.reverse_vert *= -1

    def reset_ball(self):
        self.x = self.screen_rect.right/2
        self.y = self.screen_rect.bottom/2
