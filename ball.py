# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import pygame
import time
import pygame.mixer
from pygame.sprite import Sprite
import functions as func
import random


class Ball(Sprite):

    def __init__(self, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.winner = True
        self.point = pygame.mixer.Sound('sounds\scored.wav')
        self.ping = pygame.mixer.Sound('sounds\ping.wav')

        self.image = pygame.image.load('ball_img.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.right/2
        self.rect.top = self.screen_rect.bottom/2

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = (0, 0, 0)

        self.reverse_hori = 1
        self.reverse_vert = 1
        self.velocity = 1

    def draw_ball(self):
        self.screen.blit(self.image, self.rect)

    # move ball around, bounce off objects, reset to mid screen when out of bounds
    # also stops game at 10 points
    def update_ball(self, ai_settings, paddles, score):
        if score.left_score < score.right_score:
            self.winner = False
        else:
            self.winner = True
        if self.check_hori_edges(paddles, score):
            if score.left_score < 15 and score.right_score < 15:
                self.reset_ball()
                time.sleep(0.65)
            else:
                ai_settings.game_active = False
                func.reset_game(score, self, paddles, self.screen)
        if self.check_vert_edges(paddles, score):
            if score.left_score < 15 and score.right_score < 15:
                self.reset_ball()
                time.sleep(0.65)
            else:
                ai_settings.game_active = False
                func.reset_game(score, self, paddles, self.screen)

        self.x += self.reverse_hori * self.velocity
        self.y += self.reverse_vert * self.velocity

        self.rect.x = self.x
        self.rect.y = self.y

    # ball checks if out of bounds or about to bounce off paddle, out of bounds = point increase
    def check_hori_edges(self, paddles, score):
        if self.rect.right >= self.screen_rect.right:
            self.point.play()
            score.left_score += 1
            return True
        if self.rect.left <= 0:
            self.point.play()
            score.right_score += 1
            return True
        pad = pygame.sprite.spritecollideany(self, paddles)
        if pad and pad.vertical:
            self.ping.play()
            self.reverse_hori *= -1
        return False

    # bounces off top and bottom paddles and increases points
    def check_vert_edges(self, paddles, score):
        pad = pygame.sprite.spritecollideany(self, paddles)
        if pad and not pad.vertical:
            self.ping.play()
            self.reverse_vert *= -1
            return False
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            self.point.play()
            if self.rect.left >= self.screen_rect.centerx:
                score.left_score += 1
            else:
                score.right_score += 1
            return True
        return False

    def reset_ball(self):
        self.x = self.screen_rect.right/2
        self.y = self.screen_rect.bottom/2
        self.velocity = random.uniform(0.8, 1.5)
