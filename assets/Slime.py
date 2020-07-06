import math
import pygame


class Slime(pygame.sprite.Sprite):

    def __init__(self, positionX, positionY):
        self.slimeImg = pygame.image.load('slime.png')
        self.positionX = positionX
        self.positionY = positionY
        self.slimeX_change = 0
        self.slimeY_change = 10
        self.slime_state = "ready"

    def move(self):
        if self.positionY <= 0:  # reset to value of 480 so it can be fired again
            self.slime_state = "ready"
        if self.slime_state == "fire":
            self.fire_slime(self.positionX, self.positionY)
            self.positionY -= self.slimeY_change

    def fire_slime(self, playerX, playerY):
        if self.slime_state == "ready":
            self.positionX = int(playerX)
            self.positionY = int(playerY)
            self.slime_state = "fire"

    def update(self, screen):
        if self.slime_state == "fire":
            rect = self.slimeImg.get_rect()
            rect.center = (int(self.positionX), int(self.positionY))
            screen.blit(self.slimeImg, rect)

    def has_collided(self, enemy):
        distance = math.sqrt(math.pow(enemy.positionX - self.positionX, 2)) + \
                   (math.pow(enemy.positionY - self.positionY, 2))
        if distance < 27:
            return True
        else:
            return False

    # def has_collided(self, spriteGroup):
    #     if pygame.sprite.spritecollide(self, spriteGroup, False):
    #         return True
    #     else:
    #         return False


