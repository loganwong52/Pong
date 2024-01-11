import pygame
from random import randint

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
        self.vertical_direction = ""
        self.follow_player = ""
        self.game_started = False

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and self.direction == "game over":
            # begin/continue game
            self.rect.midleft = (20, halfway)
            self.direction == ""
            self.follow_player = ""
            self.game_started = False

        if keys[pygame.K_SPACE] and self.direction == "":
            # space key is pressed, launch ball, game actually starts
            self.direction = "right"
            self.game_started = True

        # Ball follows player before space is pressed
        if not self.game_started:
            if keys[pygame.K_UP] and self.direction == "":
                self.follow_player = "up"
                self.move_up()

            if keys[pygame.K_DOWN] and self.direction == "":
                self.follow_player = "down"
                self.move_down()

            self.follow_player = ""

    def move_right(self):
        # Moves to the right until it hits the opponent
        # while self.rect.x < w:
        self.rect.x += amount

        if self.rect.x >= w:
            # print("game over")
            self.direction = "game over"

    def move_left(self):
        # Moves to the right until it hits the opponent
        # while self.rect.x < w:
        self.rect.x -= amount

        if self.rect.x <= 0:
            # print("game over")
            self.direction = "game over"

    def move_up_or_down(self):
        """
        I'm lazy, so if ball hits top/bottom edge, it remains
        at that y-value.
        """
        # print("follow player direction: " + self.follow_player)
        if self.follow_player == "up" or self.vertical_direction == "up":
            if randint(0, 1):
                # move up by 1
                self.rect.y -= 1
            else:
                # move up by 2?
                self.rect.y -= 2
        elif self.follow_player == "down" or self.vertical_direction == "down":
            if randint(0, 1):
                # move down by 1
                self.rect.y += 1
            else:
                # move down by 2?
                self.rect.y += 2
        # self.follow_player = ""

        if self.rect.top <= 0:
            self.rect.top = 0
            self.vertical_direction = ""
        elif self.rect.bottom >= h:
            self.rect.bottom = h
            self.vertical_direction = ""

    # Make ball follow player before Space is pressed
    def move_up(self):
        self.rect.y -= amount
        if self.rect.y <= 100:
            self.rect.y = 100

    def move_down(self):
        self.rect.y += amount
        if self.rect.y > h - 100:
            self.rect.y = h - 100

    def destroy(self):
        """
        If the sprite goes too far left off screen, destroy it.
        """
        if self.rect.right <= 20 or self.rect.left >= w - 20:
            self.kill()

    def update(self, direction="", vert_dir=""):
        self.player_input()

        if direction != "" and self.direction != "game over":
            self.direction = direction

        if vert_dir == "up":
            self.vertical_direction = "up"
        elif vert_dir == "down":
            self.vertical_direction = "down"

        if self.direction == "right":
            self.move_right()
            self.move_up_or_down()
        elif self.direction == "left":
            self.move_left()
            self.move_up_or_down()
