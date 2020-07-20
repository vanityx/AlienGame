import pygame

import random
from pygame import mixer


class Player(object):

    def __init__(self, positionX, positionY):
        self.playerSprite = pygame.image.load('alien2.png')
        self.positionX = positionX
        self.positionY = positionY
        self.playerX_change = 0
        self.playerY_change = 40

    def update(self, screen):
        rect = self.playerSprite.get_rect(center=(int(self.positionX), int(self.positionY)))
        rect.center = (int(self.positionX), int(self.positionY))
        screen.blit(self.playerSprite, rect)

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


class Slime(pygame.sprite.Sprite):

    def __init__(self, positionX, positionY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('slime.png')  # basic projectile sprite
        self.rect = self.image.get_rect()
        self.rect.x = positionX
        self.rect.y = positionY
        self.slimeX_change = 0
        self.slimeY_change = 5
        self.slime_state = "ready"

    def move(self):
        if self.rect.y <= 0:  # reset so it can be fired again
            self.slime_state = "ready"
            self.reset_pos()
        if self.slime_state == "fire":
            self.fire_slime(self.rect.x, self.rect.y)
            self.rect.y -= self.slimeY_change

    def fire_slime(self, playerX, playerY):
        if self.slime_state == "ready":
            self.rect.x = int(playerX)
            self.rect.y = int(playerY)
            self.slime_state = "fire"

    def update(self, screen):
        if self.slime_state == "fire":
            x = int(self.rect.x)
            y = int(self.rect.y)
            screen.blit(self.image, (x, y))

    def has_collided(self, enemy):
        if pygame.sprite.collide_rect(self, enemy):
            slime_noise = mixer.Sound('slime_noise.wav')
            slime_noise.play()
            return True

    def reset_pos(self):
        self.rect.x = 400
        self.rect.y = 569


class Enemy(pygame.sprite.Sprite):

    def __init__(self, positionX, positionY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ice-cream.png')  # basic enemy sprite
        self.rect = self.image.get_rect()
        self.rect.x = positionX
        self.rect.y = positionY
        self.enemyX_change = 8
        self.enemyY_change = 40

    def update(self, screen):
        self.move(screen)
        x = int(self.rect.x)
        y = int(self.rect.y)

        screen.blit(self.image, (x, y))

    def move(self, screen):

        self.rect.x += self.enemyX_change
        screen_width = int(screen.get_width())
        right_boundary = screen_width - 20
        left_boundary = 20
        if self.rect.x <= left_boundary:
            self.enemyX_change = 8
            self.rect.y += self.enemyY_change
        if self.rect.x >= right_boundary:
            self.enemyX_change = -8
            self.rect.y += self.enemyY_change

        return self.rect.x, self.rect.y

    def get_position(self):
        return self.rect.x, self.rect.y

    # reset random position
    def reset(self, screen):
        self.rect.x = random.randint(0, int(screen.get_width()))
        self.rect.y = random.randint(0, int((screen.get_height() / 2) - 30))
