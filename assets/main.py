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
# playerImg = pygame.image.load('alien2.png')
# playerX = 370
# playerY = 480
# playerX_change = 0

player = Player(370, 480)

# enemy
enemy = Enemy(random.randint(0, 735), random.randint(50, 150))

# slime
slime = Slime(0,480)

# ready state - can't see slime on screen
# fire state - slime is currently moving
# slimeImg = pygame.image.load('slime.png')
# slimeX = 0
# slimeY = 480
# slimeX_change = 0
# slimeY_change = 10
# slime_state = "ready"

score = 0

# def fire_slime(x, y):
#     global slime_state
#     x = int(x)
#     y = int(y)
#     slime_state = "fire"
#     screen.blit(slimeImg, (x + 16, y + 10))


def has_collided(enemyX, enemyY, slimeX, slimeY):
    distance = math.sqrt(math.pow(enemyX - slimeX, 2)) + (math.pow(enemyY - slimeY, 2))
    if distance < 27:
        return True
    else:
        return False


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

        enemy.update(screen)
        player.update(screen, event)
        slime.move(screen, event, player.positionX)

        # keystroke activation
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         playerX_change = -8
        #     if event.key == pygame.K_RIGHT:
        #         playerX_change = 8
        #     if event.key == pygame.K_SPACE:
        #         slimeX = playerX
        #         fire_slime(slimeX, slimeY)

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         playerX_change = 0

        # checking for boundaries so they don't go out of bounds
        #         # player movement
        #         # playerX += playerX_change
        #         #
        #         # if playerX <= 0:
        #         #     playerX = 0
        #         # elif playerX >= 736:
        #         #     playerX = 736
        #
        #         # slime movement
        #         # if slimeY <= 0:  # reset to value of 480 so it can be fired again
        #         #     slimeY = 480
        #         #     slime_state = "ready"
        #         # if slime_state == "fire":
        #         #     fire_slime(slimeX, slimeY)
        #         #     slimeY -= slimeY_change
        #
        #         # what to do if collision has occured

        # collision = has_collided(enemy.positionX,enemy.positionY,slime.positionX,slime.positionY)
        # if collision:
        #      slime.slimeY = 480
        #      slime.slime_state = "ready"
        #      score += 1
        #      print(score)
        #      enemy.reset()

        player.check()
        pygame.display.update()

        # Flip everything to the display
        pygame.display.flip()

        # Ensure program maintains a rate of 60 frames per second
        clock.tick(60)
