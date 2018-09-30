# Raul Cerda
# raul.cerda@csu.fullerton.edu
# Project 2: Pong

import sys
import pygame.font
import pygame
from paddles import Paddle


# creates paddle on both sides and adds to group to move together
def create_paddles(screen, ball, paddles):
    paddle_l = Paddle(screen, ball, True, True)
    paddles.add(paddle_l)
    paddle_r = Paddle(screen, ball, True, False)
    paddle_r.rect.right = screen.get_rect().right - 3
    paddles.add(paddle_r)

    paddle_top_left = Paddle(screen, ball, False, True)
    paddles.add(paddle_top_left)
    paddle_top_right = Paddle(screen, ball, False, False)
    paddle_top_right.rect.centerx = int(screen.get_rect().right * 0.75)
    paddle_top_right.x = paddle_top_right.rect.x
    paddles.add(paddle_top_right)

    paddle_bot_left = Paddle(screen, ball, False, True)
    paddle_bot_left.rect.centery = screen.get_rect().bottom - 10
    paddles.add(paddle_bot_left)
    paddle_bot_right = Paddle(screen, ball, False, False)
    paddle_bot_right.rect.centerx = int(screen.get_rect().right * 0.75)
    paddle_bot_right.rect.centery = int(screen.get_rect().bottom - 10)
    paddle_bot_right.x = paddle_bot_right.rect.x
    paddles.add(paddle_bot_right)


def draw_half_line(screen):
    j = 0
    for i in range(0, int(screen.get_rect().bottom/70)):
        segment = pygame.Rect(screen.get_rect().right/2, j, 10, 50)
        j += 70
        pygame.draw.rect(screen, (20, 20, 20), segment)


# if game ongoing, update elements and draw them, otherwise show title and button
def update_screen(ai_settings, screen, ball, paddles, score, play_but, first_time):
    if ai_settings.game_active:
        screen.fill(ai_settings.bg_color)
        draw_half_line(screen)
        ball.update_ball(ai_settings, paddles, score)
        ball.draw_ball()
        paddles.draw(screen)
        score.show_scores()

    if not ai_settings.game_active:
        pygame.mouse.set_visible(True)
        play_but.show_inactive_menu(first_time, ball.winner)
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
                    if paddle.left_side:
                        paddle.moving_up = True
            elif event.key == pygame.K_DOWN:
                for paddle in paddles:
                    if paddle.left_side:
                        paddle.moving_down = True
            elif event.key == pygame.K_LEFT:
                for paddle in paddles:
                    if paddle.left_side:
                        paddle.moving_left = True
            elif event.key == pygame.K_RIGHT:
                for paddle in paddles:
                    if paddle.left_side:
                        paddle.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                for paddle in paddles:
                    paddle.moving_up = False
            elif event.key == pygame.K_DOWN:
                for paddle in paddles:
                    paddle.moving_down = False
            elif event.key == pygame.K_LEFT:
                for paddle in paddles:
                    paddle.moving_left = False
            elif event.key == pygame.K_RIGHT:
                for paddle in paddles:
                    paddle.moving_right = False

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
        if paddle.vertical:
            paddle.rect.centery = screen.get_rect().bottom/2
        elif paddle.left_side:
            paddle.rect.centerx = screen.get_rect().right/4
        else:
            paddle.rect.centerx = int(screen.get_rect().right * 0.75)


def show_winner(screen, winner):
    win_font = pygame.font.SysFont(None, 150)

    if winner:
        win_img = win_font.render('Player 1 Wins', True, (50, 255, 50), (0, 0, 0))
    else:
        win_img = win_font.render('Computer Wins', True, (50, 255, 50), (0, 0, 0))
    win_rect = win_img.get_rect()
    win_rect.centerx = screen.get_rect().centerx
    win_rect.centery = screen.get_rect().centery/2
    screen.blit(win_img, win_rect)
