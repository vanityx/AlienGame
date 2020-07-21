import sys
from enum import Enum

import pygame


class Scoreboard:

    def __init__(self):
        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.textX = 10
        self.textY = 10
        self.over_font = pygame.font.Font('freesansbold.ttf', 100)
        self.won_font = pygame.font.Font('freesansbold.ttf', 100)
        self.replay_font = pygame.font.Font('freesansbold.ttf', 20)

    def show_score(self, screen):
        score_text = self.font.render("Score: " + str(self.score_value), True, (255, 255, 255))
        screen.blit(score_text, (self.textX, self.textY))

    def check_game_end(self, screen, enemy):
        if self.score_value >= 10:
            self.game_won_text(screen)
            return True
        if enemy > int(screen.get_height() - 200):
            self.game_over_text(screen)
            return True

    def game_won_text(self, screen):
        won_text = self.won_font.render("YOU WIN", True, (255, 255, 255))
        replay_text = self.replay_font.render("Press 'R' To Play Again", True, (255, 255, 255))
        rect1 = won_text.get_rect(center=(int(screen.get_width() / 2), int(screen.get_height() / 2)))
        rect2 = replay_text.get_rect(center=(int(screen.get_width() / 2), int(screen.get_height() / 2) + 70))
        screen.blit(won_text, rect1)
        screen.blit(replay_text, rect2)

    def game_over_text(self, screen):
        over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))
        replay_text = self.replay_font.render("Press 'R' To Play Again", True, (255, 255, 255))
        rect1 = over_text.get_rect(center=(int(screen.get_width() / 2), int(screen.get_height() / 2)))
        rect2 = replay_text.get_rect(center=(int(screen.get_width() / 2), int(screen.get_height() / 2) + 70))
        screen.blit(over_text, rect1)
        screen.blit(replay_text, rect2)


class ControllerState(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    SPACE = 3
    RESTART_KEY = 4
    KEY_RELEASE = 5


class playerInput:
    def __init__(self):
        self.game_running = True
        self.controller_state = ControllerState.NONE

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.controller_state = ControllerState.LEFT
                if event.key == pygame.K_RIGHT:
                    self.controller_state = ControllerState.RIGHT
                if event.key == pygame.K_SPACE:
                    self.controller_state = ControllerState.SPACE
                if event.key == pygame.K_r:
                    self.controller_state = ControllerState.RESTART_KEY
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.controller_state = ControllerState.KEY_RELEASE
