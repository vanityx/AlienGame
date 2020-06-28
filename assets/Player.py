import pygame


class Player:

    def __init__(self, positionX, positionY):
        self.playerImg = pygame.image.load('alien2.png')
        self.positionX = positionX
        self.positionY = positionY
        self.playerX_change = 0
        self.playerY_change = 40

    def update(self, screen):
        rect = self.playerImg.get_rect(center=(int(self.positionX), int(self.positionY)))
        rect.center = (int(self.positionX), int(self.positionY))
        screen.blit(self.playerImg, rect)

    def move(self, playerX_change):
        self.playerX_change = int(playerX_change)

    def check(self):
        self.positionX += self.playerX_change
        if self.positionX <= 0:
            self.positionX = 0
        elif self.positionX >= 736:
            self.positionX = 736

    def get_position(self):
        return self.positionX

