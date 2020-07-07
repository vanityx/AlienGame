import math
import pygame


class Slime(pygame.sprite.Sprite):

    def __init__(self, positionX, positionY):
        pygame.sprite.Sprite.__init__(self)
        self.slimeSprite = pygame.image.load('slime.png') # basic projectile sprite
        self.positionX = positionX
        self.positionY = positionY
        self.width = int(self.slimeSprite.get_width())
        self.height = int(self.slimeSprite.get_height())
        self.rect = pygame.Rect(self.positionX, self.positionY, self.width, self.height)
        self.slimeX_change = 0
        self.slimeY_change = 5
        self.hitbox = (self.positionX, self.positionY, self.width, self.height)
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
            # rect = self.slimeSprite.get_rect()
            # rect.center = (int(self.positionX), int(self.positionY))
            # screen.blit(self.slimeSprite, rect)

            x = int(self.positionX)
            y = int(self.positionY)
            screen.blit(self.slimeSprite, (x,y))

            # show hitbox
            # self.hitbox = (self.positionX, self.positionY, self.width, self.height)
            # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def has_collided(self, enemy_rect):
        self.rect = pygame.Rect(self.positionX, self.positionY, self.width, self.height)
        if self.rect.colliderect(enemy_rect):
            return True

    # def has_collided(self, enemy):
    #     distance = math.sqrt(math.pow(enemy.positionX - self.positionX, 2)) + \
    #                (math.pow(enemy.positionY - self.positionY, 2))
    #     if distance < 27:
    #         return True
    #     else:
    #         return False