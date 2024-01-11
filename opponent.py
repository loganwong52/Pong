import pygame
from sys import exit
from random import randint, choice

w = 640
h = 480
halfway = h / 2
choices = ["ball", "ball", "ball", "no"]
amount = 5


class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.amount = amount
        self.image = pygame.Surface((20, 200))
        self.image.fill("red")
        self.rect = self.image.get_rect(midright=(w, halfway))
        self.direction = ""

    def movement(self):
        # Only call this if top is at 0 or bottom is at h
        # if self.rect.top == 0 or self.rect.bottom == h:
        # direction = randint(0, 1)
        # print(direction)
        # if direction:
        # if 1, move up
        # while self.rect.top != 0:
        #     self.rect.y -= self.amount
        # self.rect.y = 0
        if self.rect.top <= 0:
            self.rect.top = 0
            # change direction
            self.amount = amount
        else:
            # move down
            # while self.rect.bottom != h:
            # self.rect.y += self.amount
            # self.rect.y = h
            if self.rect.bottom >= h:
                self.rect.bottom = h
                self.amount = -1 * amount

    def update(self):
        self.movement()
        self.rect.y += self.amount
        if self.amount:
            self.direction = "down"
        else:
            self.direction = "up"
