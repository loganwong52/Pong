import pygame
from sys import exit
from random import randint, choice

w = 640
h = 480
halfway = h / 2
choices = ["ball", "ball", "ball", "no"]


class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.amount = 10
        self.image = pygame.Surface((20, 200))
        self.image.fill("red")
        self.rect = self.image.get_rect(midright=(w, halfway))

    def movement(self):
        if randint(0, 2):
            # if 1, move up
            self.rect.y -= self.amount
            if self.rect.top <= 0:
                self.rect.top = 0
        else:
            self.rect.y += self.amount
            if self.rect.bottom >= h:
                self.rect.bottom = h

    def update(self):
        # self.movement()
        pass
