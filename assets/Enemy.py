import pygame
import random

# list of all 'enemies'
# each enemy is added to this list, which is managed by a class called 'Group'
enemy_list = pygame.sprite.Group()

# this is a list of every sprite/enemy
all_sprites_list = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):

    def __init__(self, positionX, positionY):
        self.enemyImg = pygame.image.load('ice-cream.png')
        self.positionX = positionX
        self.positionY = positionY
        self.enemyX_change = 6
        self.enemyY_change = 40
        self.num_enemies = 6

    def update(self, screen):
        self.move()
        for i in range(self.num_enemies):
            x = int(self.positionX)
            y = int(self.positionY)

        screen.blit(self.enemyImg, (x, y))

    def move(self):

        self.positionX += self.enemyX_change
        if self.positionX <= 0:
            self.enemyX_change = 4
            self.positionY += self.enemyY_change
        elif self.positionX >= 736:
            self.enemyX_change = -4
            self.positionY += self.enemyY_change

            return self.positionX, self.positionY

    def get_position(self):
        return self.positionX, self.positionY

    # reset random position
    def reset(self):
        self.positionX = random.randint(0, 800)
        self.positionY = random.randint(50, 150)
