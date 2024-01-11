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
        if keys[pygame.K_SPACE] and self.direction == "":
            # space key is pressed, launch ball
            self.direction = "right"

    def move_right(self):
        # Moves to the right until it hits the opponent
        # while self.rect.x < w:
        self.rect.x += amount

        if self.rect.x >= w:
            print("game over")
            self.direction = "game over"

    def move_left(self):
        # Moves to the right until it hits the opponent
        # while self.rect.x < w:
        self.rect.x -= amount

        if self.rect.x <= 0:
            print("game over")
            self.direction = "game over"

    def change_direction(self, direction):
        print("i am direction: " + direction)
        # Called when ball hits player or opponent
        self.direction = direction

    def update(self, direction=""):
        self.player_input()

        if direction != "" and self.direction != "game over":
            self.direction = direction

        if self.direction == "right":
            self.move_right()
        elif self.direction == "left":
            self.move_left()
