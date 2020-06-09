import pygame
import random


class Enemy:
    enemyImg = pygame.image.load('ice-cream.png')
    positionX = 0
    positionY = 0
    enemyX_change = 0
    enemyY_change = 0

    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY
        self.enemyX_change = 2.5
        self.enemyY_change = 40

    def update(self, screen):
        self.move()
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

    def get_position(self):
        return self.positionX, self.positionY

    # reset random position
    def reset(self):
        self.positionX = random.randint(0, 800)
        self.positionY = random.randint(50, 150)
