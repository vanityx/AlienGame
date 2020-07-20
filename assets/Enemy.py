import pygame
import random


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
