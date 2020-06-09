import pygame


class Slime:
    slimeImg = pygame.image.load('slime.png')
    positionX = 0
    positionY = 480
    slimeX_change = 0
    slimeY_change = 0
    slime_state = "ready"

    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY
        self.slimeX_change = 0
        self.slimeY_change = 10

    def move(self, screen, event, playerX):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.positionX = playerX
                self.fire_slime(screen, self.positionX, self.positionY)
            if self.positionY <= 0:  # reset to value of 480 so it can be fired again
                self.positionY = 480
                self.slime_state = "ready"
            if self.slime_state == "fire":
                self.fire_slime(screen, self.positionX, self.positionY)
                self.positionY -= self.slimeY_change

    def fire_slime(self, screen, positionX, positionY):
        x = int(positionX)
        y = int(positionY)
        self.slime_state = "fire"
        screen.blit(self.slimeImg, (x + 16, y + 10))
