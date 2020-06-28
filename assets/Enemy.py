import pygame
import random


class Enemy:

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
        if self.positionY > 440:
            self.positionY = 2000
            from assets.main import game_over_text
            game_over_text()

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

