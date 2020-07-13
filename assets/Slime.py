import pygame


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
            return True

    def reset_pos(self):
        self.rect.x = 400
        self.rect.y = 569