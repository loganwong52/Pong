import pygame

w = 640
h = 480
halfway = h / 2
amount = 10


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((20, 20))
        self.image.fill("Yellow")
        self.rect = self.image.get_rect(midleft=(20, halfway))

        self.direction = ""

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            # space key is pressed, launch ball
            self.direction = "right"

    def move_right(self):
        # Moves to the right until it hits the opponent
        # while self.rect.x < w:
        self.rect.x += amount

        if self.rect.x >= w:
            print("game over")
            self.direction = ""

    def update(self):
        self.player_input()

        if self.direction == "right":
            self.move_right()
        elif self.direction == "left":
            # self.move_left()
            pass
