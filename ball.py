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
            # space key is pressed, launch ball, game actuall starts
            self.direction = "right"
            self.game_started = True

        # Ball follows player before space is pressed
        if not self.game_started:
            if keys[pygame.K_UP] and self.direction == "":
                self.follow_player = "up"
            if keys[pygame.K_DOWN] and self.direction == "":
                self.follow_player = "down"

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

    def update(self, direction=""):
        self.player_input()

        if direction != "" and self.direction != "game over":
            self.direction = direction

        if self.direction == "right":
            self.move_right()
        elif self.direction == "left":
            self.move_left()

        if not self.game_started:
            # check if up/down keys pressed
            if self.follow_player == "up":
                self.move_up()
            elif self.follow_player == "down":
                self.move_down()
            self.follow_player = ""
