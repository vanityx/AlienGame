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
background = pygame.image.load('2399.png')

# title and icon
pygame.display.set_caption("Alien vs Ice Cream ")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# player
player = Player(400, 520)

# enemy
enemy = Enemy(random.randint(0, 735), random.randint(50, 150))

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
                player.move(-8)
            if event.key == pygame.K_RIGHT:
                player.move(8)
            if event.key == pygame.K_SPACE:
                slime.fire_slime(player.positionX, player.positionY)
            if event.key == pygame.K_r:
                game_ended = False
                scoreboard.score_value = 0
                enemy.reset()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.move(0)

    if not game_ended:

        slime.move()
        slime.update(screen)
        player.update(screen)
        enemy.update(screen)
        player.check()
        pygame.display.update()
        scoreboard.show_score(screen)
        if scoreboard.check_game_end(screen, enemy.positionY):
            game_ended = True

        # what to do if collision has occurs
        collision = slime.has_collided(enemy)
        if collision:
            slime.slime_state = "ready"
            scoreboard.score_value += 1
            print(scoreboard.score_value)
            enemy.reset()

        # Flip everything to the display
        pygame.display.flip()

        # Ensure program maintains a rate of 60 frames per second
        clock.tick(60)
