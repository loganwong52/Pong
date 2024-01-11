import pygame

w = 640
h = 480
halfway = h / 2


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((20, 20))
        self.image.fill("Yellow")
        self.rect = self.image.get_rect(center=(w / 2, halfway))

    def update(self):
        pass
