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

    def check(self, screen):
        screen_width = int(screen.get_width())
        right_boundary = screen_width - 50
        left_boundary = 50
        self.positionX += self.playerX_change
        if self.positionX <= left_boundary:
            self.positionX = left_boundary
        elif self.positionX >= right_boundary:
            self.positionX = right_boundary

    def get_position(self):
        return self.positionX

