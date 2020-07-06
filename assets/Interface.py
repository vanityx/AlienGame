import pygame
import math

class Interface:

    def __init__(self):
        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.textX = 10
        self.textY = 10
        self.over_font = pygame.font.Font('freesansbold.ttf', 100)
        self.won_font = pygame.font.Font('freesansbold.ttf', 100)
        self.replay_font = pygame.font.Font('freesansbold.ttf', 20)

    def show_score(self, self.textX, self.textY, screen):
        score = self.font.render("Score: " + str(self.score_value), True, (255, 255, 255))
        screen.blit(score, (self.textX, self.textY))

    def check_score(self, score_value):
        if score_value >= 3:
            game_won_text()
            return True
        else:
            return False

    def check_enemy_pos(self, enemy):
        if enemy.positionY > 200:
            enemy.positionY = 2000
            game_over_text()
            return True
        else:
            return False

    def game_won_text(self, screen):
        won_text = won_font.render("YOU WIN", True, (255, 255, 255))
        replay_text = replay_font.render("Press 'R' To Play Again", True, (255, 255, 255))
        rect1 = won_text.get_rect(center=(int(screen.get_width() / 2), int(screen.get_height() / 2)))
        rect2 = replay_text.get_rect(center=(int(screen.get_width() / 2), int(screen.get_height() / 2) + 70))
        screen.blit(won_text, rect1)
        screen.blit(replay_text, rect2)

    def game_over_text(self, screen):
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        replay_text = replay_font.render("Press 'R' To Play Again", True, (255, 255, 255))
        rect1 = over_text.get_rect(center=(int(screen.get_width() / 2), int(screen.get_height() / 2)))
        rect2 = replay_text.get_rect(center=(int(screen.get_width() / 2), int(screen.get_height() / 2) + 70))
        screen.blit(over_text, rect1)
        screen.blit(replay_text, rect2)
