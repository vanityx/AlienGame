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


# class KeyboardInput:
#     def __init__(self):
#         self.game_running = True
#         self.restart_game = False
#
#     def movement(self, event):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.game_running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     player.move(-8)
#                 if event.key == pygame.K_RIGHT:
#                     player.move(8)
#                 if event.key == pygame.K_SPACE:
#                     slime.fire_slime(player.positionX, player.positionY)
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     player.move(0)
#
#     def restart(self):
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_r:
#                     self.restart_game = True
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     player.move(0)

# store a state in the controller, in the keyboard input class