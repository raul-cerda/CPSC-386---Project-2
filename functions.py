# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import sys
import pygame
from paddles import Paddle


# creates paddle on both sides and adds to group to move together
def create_paddles(screen, paddles):
    paddle_l = Paddle(screen)
    paddles.add(paddle_l)
    paddle_r = Paddle(screen)
    paddle_r.rect.right = screen.get_rect().right - 3
    paddles.add(paddle_r)


def draw_half_line(screen):
    j = 0
    for i in range(0, int(screen.get_rect().bottom/100)):
        segment = pygame.Rect(screen.get_rect().right/2, j, 10, 90)
        j += 110
        pygame.draw.rect(screen, (20, 20, 20), segment)


# if game ongoing, update elements and draw them, otherwise show title and button
def update_screen(ai_settings, screen, ball, paddles, score, play_but):
    if ai_settings.game_active:
        screen.fill(ai_settings.bg_color)
        draw_half_line(screen)
        ball.update_ball(ai_settings, paddles, score)
        ball.draw_ball()
        paddles.draw(screen)
        score.show_scores()

    if not ai_settings.game_active:
        pygame.mouse.set_visible(True)
        play_but.show_inactive_menu()
    pygame.display.flip()


# all controls here, paddles and play button
def check_events(ai_settings, paddles, play_but):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_UP:
                for paddle in paddles:
                    paddle.moving_up = True
            elif event.key == pygame.K_DOWN:
                for paddle in paddles:
                    paddle.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                for paddle in paddles:
                    paddle.moving_up = False
            elif event.key == pygame.K_DOWN:
                for paddle in paddles:
                    paddle.moving_down = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, play_but, mouse_x, mouse_y)


# start game when pressing play
def check_play_button(ai_settings, play_but, mouse_x, mouse_y):
    button_pressed = play_but.rect.collidepoint(mouse_x, mouse_y)
    if button_pressed and not ai_settings.game_active:
        pygame.mouse.set_visible(False)
        ai_settings.game_active = True


# set everything to default when game is over
def reset_game(score, ball, paddles, screen):
    score.left_score = 0
    score.right_score = 0
    ball.reset_ball()
    for paddle in paddles:
        paddle.rect.centery = screen.get_rect().bottom/2
