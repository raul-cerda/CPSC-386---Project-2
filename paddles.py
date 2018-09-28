# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    def __init__(self, screen):
        super(Paddle, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, 20, 120)
        self.image = pygame.Surface((20, 120))
        self.rect.left = self.screen_rect.left + 3
        self.rect.centery = self.screen_rect.bottom/2

        self.color = (0, 0, 0)

        self.moving_up = False
        self.moving_down = False

    # uses moving boolean for continuous movement
    def update(self):
        if self.moving_up and self.rect.top >= 0:
            self.rect.y -= 2
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.y += 2
