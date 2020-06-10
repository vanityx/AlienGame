import pygame
import math
import random
from Enemy import Enemy
from Player import Player
from Slime import Slime

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
score = 0

# game loop / makes sure everything appears
running = True
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.move(0)

    slime.move()
    slime.update(screen)
    player.update(screen)
    enemy.update(screen)
    player.check()
    pygame.display.update()

    # what to do if collision has occurs

    collision = slime.has_collided(enemy)
    if collision:
        slime.slime_state = "ready"
        score += 1
        print(score)
        enemy.reset()

    # Flip everything to the display
    pygame.display.flip()

    # Ensure program maintains a rate of 60 frames per second
    clock.tick(60)
