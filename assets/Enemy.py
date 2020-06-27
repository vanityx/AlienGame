import pygame
import random

class Enemy:

    def __init__(self, positionX, positionY):
        self.enemyImg = []
        self.positionX = []
        self.positionY = []
        self.enemyX_change = []
        self.enemyY_change = []
        self.num_enemies = 6

        for i in range(self.num_enemies):
            self.enemyImg.append(pygame.image.load('ice-cream.png'))
            self.positionX.append(positionX)
            self.positionY.append(positionY)
            self.enemyX_change.append(6)
            self.enemyY_change.append(40)

    def update(self, screen):
        self.move()
        for i in range(self.num_enemies):
            x = int(self.positionX[i])
            y = int(self.positionY[i])

        screen.blit(self.enemyImg[i], (x, y))

    def move(self):

        for i in range(self.num_enemies):
            self.positionX[i] += self.enemyX_change[i]
            if self.positionX[i] <= 0:
                self.enemyX_change[i] = 4
                self.positionY[i] += self.enemyY_change[i]
            elif self.positionX[i] >= 736:
                self.enemyX_change[i] = -4
                self.positionY[i] += self.enemyY_change[i]

            return self.positionX[i], self.positionY[i]

    def get_position(self):
        return self.positionX, self.positionY

    # reset random position
    def reset(self):
        self.positionX = random.randint(0, 800)
        self.positionY = random.randint(50, 150)
