import pygame
from sys import exit

w = 640
h = 480
halfway = h / 2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.amount = 10
        self.image = pygame.Surface((20, 200))
        self.image.fill("White")
        self.rect = self.image.get_rect(midleft=(0, halfway))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.amount
            if self.rect.top <= 0:
                self.rect.top = 0

        if keys[pygame.K_DOWN]:
            self.rect.y += self.amount
            if self.rect.bottom >= h:
                self.rect.bottom = h

    def update(self):
        self.player_input()
