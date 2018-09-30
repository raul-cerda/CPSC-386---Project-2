# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    def __init__(self, screen, ball, vertical, left_side):
        super(Paddle, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ball = ball
        self.vertical = vertical
        self.left_side = left_side
        self.color = (0, 0, 0)

        if self.vertical:
            self.rect = pygame.Rect(0, 0, 20, 120)
            self.image = pygame.Surface((20, 120))
            self.rect.left = self.screen_rect.left + 3
            self.rect.centery = self.screen_rect.bottom/2
        else:
            self.rect = pygame.Rect(0, 0, 120, 20)
            self.image = pygame.Surface((120, 20))
            self.rect.left = self.screen_rect.right/4
            self.rect.centery = self.screen_rect.top + 10

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        if self.left_side:
            self.x_speed = 1
            self.y_speed = 2
        else:
            self.x_speed = 0.75
            self.y_speed = 0.75

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # uses moving boolean for continuous movement
    def update(self):
        if not self.left_side:
            self.ai_update_vert()
            self.ai_update_hori()
        if self.vertical:
            if self.moving_up and self.rect.top >= 0:
                self.y -= self.y_speed
                self.rect.y = self.y
            if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
                self.y += self.y_speed
                self.rect.y = self.y
        elif self.left_side:
            if self.moving_left and self.rect.left >= 0:
                self.rect.x -= self.x_speed
            if self.moving_right and self.rect.right <= self.screen_rect.right/2:
                self.rect.x += self.x_speed
        else:
            if self.moving_left and self.rect.left >= self.screen_rect.right/2:
                self.x -= self.x_speed
                self.rect.x = self.x
            if self.moving_right and self.rect.right <= self.screen_rect.right:
                self.x += self.x_speed
                self.rect.x = self.x

    def ai_update_vert(self):
        if self.rect.centery > self.ball.rect.centery:
            self.moving_up = True
            self.moving_down = False
        if self.rect.centery < self.ball.rect.centery:
            self.moving_down = True
            self.moving_up = False

    def ai_update_hori(self):
        if self.rect.centerx > self.ball.rect.centerx:
            self.moving_left = True
            self.moving_right = False
        if self.rect.centerx < self.ball.rect.centerx:
            self.moving_right = True
            self.moving_left = False
