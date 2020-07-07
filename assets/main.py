import random

import pygame

from assets.Enemy import Enemy
from assets.Player import Player
from assets.Slime import Slime
from assets.Interface import Scoreboard

# initialise the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# clock
clock = pygame.time.Clock()

# add background image
background = pygame.image.load('background.png')

# title and icon
pygame.display.set_caption("Alien vs Ice Cream ")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# player
player = Player(400, 520)

# enemies
enemy1 = Enemy(random.randint(0, int(screen.get_width())), random.randint(0, int(screen.get_height() / 2)))
enemy2 = Enemy(random.randint(0, int(screen.get_width())), random.randint(0, int(screen.get_height() / 2)))
enemy3 = Enemy(random.randint(0, int(screen.get_width())), random.randint(0, int(screen.get_height() / 2)))
enemy4 = Enemy(random.randint(0, int(screen.get_width())), random.randint(0, int(screen.get_height() / 2)))

enemies = [enemy1, enemy2, enemy3, enemy4]

# slime
slime = Slime(0, 480)

# scoreboard
scoreboard = Scoreboard()

# game loop / makes sure everything appears
running = True
game_ended = False
while running:

    # RGB values
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(-4)
            if event.key == pygame.K_RIGHT:
                player.move(4)
            if event.key == pygame.K_SPACE:
                slime.fire_slime(player.positionX, player.positionY)
            if event.key == pygame.K_r:
                game_ended = False
                scoreboard.score_value = 0
                for enemy in enemies:
                    enemy.reset(screen)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.move(0)

    if not game_ended:
        for enemy in enemies:

            slime.move()
            slime.update(screen)
            player.update(screen)
            enemy.update(screen)
            player.check(screen)
            pygame.display.update()
            scoreboard.show_score(screen)
            if scoreboard.check_game_end(screen, enemy.positionY):
                game_ended = True

            # what to do if collision has occurs
            enemy_rect = enemy.get_enemy_rect()
            if slime.has_collided(enemy_rect):
                slime.slime_state = "ready"
                scoreboard.score_value += 1
                print(scoreboard.score_value)
                enemy.reset(screen)

        # Flip everything to the display
        pygame.display.flip()

        # Ensure program maintains a rate of 60 frames per second
        clock.tick(60)
