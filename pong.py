# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import pygame
from settings import Settings
from ball import Ball
from scores import Scores
from pygame.sprite import Group
from button import Button
import functions as func


# main game loop; checks if game is active for display/hiding menu
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pong")

    play_but = Button(screen, 'Play')
    ball = Ball(screen)
    paddles = Group()
    score = Scores(screen)
    func.create_paddles(screen, paddles)

    while True:
        func.check_events(ai_settings, paddles, play_but)
        if ai_settings.game_active:
            paddles.update()
        func.update_screen(ai_settings, screen, ball, paddles, score, play_but)


run_game()
