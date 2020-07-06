import pygame
import random

# list of all 'enemies'
# each enemy is added to this list, which is managed by a class called 'Group'
enemy_list = pygame.sprite.Group()

# this is a list of every sprite/enemy
all_sprites_list = pygame.sprite.Group()


class Enemy(object):

    def __init__(self, positionX, positionY):
        self.enemySprite = pygame.image.load('ice-cream.png')  # basic enemy sprite
        self.positionX = positionX
        self.positionY = positionY
        self.width = int(self.enemySprite.get_width())
        self.height = int(self.enemySprite.get_height())
        self.enemyX_change = 6
        self.enemyY_change = 40
        self.hitbox = (self.positionX, self.positionY, self.width, self.height)


    def update(self, screen):
        self.move(screen)
        x = int(self.positionX)
        y = int(self.positionY)

        screen.blit(self.enemySprite, (x, y))

        # show hitbox
        self.hitbox = (self.positionX, self.positionY, self.width, self.height)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


    def move(self, screen):

        self.positionX += self.enemyX_change
        screen_width = int(screen.get_width())
        right_boundary = screen_width - 20
        left_boundary = 20
        if self.positionX <= left_boundary:
            self.enemyX_change = 4
            self.positionY += self.enemyY_change
        if self.positionX >= right_boundary:
            self.enemyX_change = -4
            self.positionY += self.enemyY_change

        return self.positionX, self.positionY

    def get_position(self):
        return self.positionX, self.positionY

    # reset random position
    def reset(self, screen):
        self.positionX = random.randint(0, int(screen.get_width()))
        self.positionY = random.randint(0, int(screen.get_height() / 2))
