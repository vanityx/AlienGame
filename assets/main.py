import pygame
import math
import random
from assets.Enemy import Enemy
from assets.Player import Player
from assets.Slime import Slime

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
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# game text
over_font = pygame.font.Font('freesansbold.ttf', 64)
won_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score = font.render("Score: " + str(score_value),True, (255,255,255))
    screen.blit(score, (x, y))

def check_score(score_value):
    if score_value >= 3:
        game_won_text()

def game_won_text():
    won_text = font.render("YOU WIN", True, (255, 255, 255))
    rect = won_text.get_rect(center=(800 / 2, 600 / 2))
    screen.blit(won_text, rect)

def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    rect = over_text.get_rect(center=(800/2, 600/2))
    screen.blit(over_text, rect)

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
    show_score(textX, textY)
    check_score(score_value)

    # what to do if collision has occurs
    collision = slime.has_collided(enemy)
    if collision:
        slime.slime_state = "ready"
        score_value += 1
        print(score_value)
        enemy.reset()

    # Flip everything to the display
    pygame.display.flip()

    # Ensure program maintains a rate of 60 frames per second
    clock.tick(60)
