import pygame


class Player:
    playerImg = pygame.image.load('alien2.png')
    positionX = 370
    positionY = 480
    playerX_change = 0
    playerY_change = 0

    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY
        self.playerX_change = 2.5
        self.playerY_change = 40

    def update(self,screen,event):
        self.move(event)
        x = int(self.positionX)
        y = int(self.positionY)
        screen.blit(self.playerImg, (x, y))

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change = -8
            if event.key == pygame.K_RIGHT:
                self.playerX_change = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.playerX_change = 0

    def check(self):
        self.positionX += self.playerX_change
        if self.positionX <= 0:
            self.positionX = 0
        elif self.positionX >= 736:
            self.positionX = 736


