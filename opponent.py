import pygame
from random import randint, choice

w = 640
h = 480
halfway = h / 2
# Old idea: Maybe 9/10 opponent goes towards ball?
# hit_choices = [
#     "ball",
#     "ball",
#     "ball",
#     "ball",
#     "ball",
#     "ball",
#     "ball",
#     "ball",
#     "ball",
#     "no",
# ]
# 10% of the time, Opp is slow
# 60% of the time, Opp is medium speed
# 20% of the time, Opp is medium fast
# 10% of the time, Opp is fast
speed_choices = [3, 5, 5, 5, 5, 5, 5, 7, 7, 8]
amount = 10


class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.amount = amount
        self.image = pygame.Surface((20, 200))
        self.image.fill("red")
        self.rect = self.image.get_rect(midright=(w, halfway))
        self.direction = ""
        self.ball_direction = ""
        self.follow_ball = False
        self.limit = h / 2
        self.follow_player = True

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and not self.follow_ball:
            # begin/continue game
            self.amount = 10

        if keys[pygame.K_SPACE]:
            self.follow_player = False

        # if keys[pygame.K_RETURN]:
        #     self.rect.midright = (w, halfway)

        if self.follow_player:
            if keys[pygame.K_UP]:
                self.rect.y -= 5
                if self.rect.top <= 0:
                    self.rect.top = 0

            if keys[pygame.K_DOWN]:
                self.rect.y += 5
                if self.rect.bottom >= h:
                    self.rect.bottom = h

    def movement(self):
        """
        If opponent hits the top, switch direction.
        If opponent hits the bottom, switch direction.
        """
        if self.rect.top <= 0:
            self.rect.top = 0
            if self.amount < 0:
                self.amount = -1 * self.amount
        else:
            # move down
            if self.rect.bottom >= h:
                self.rect.bottom = h
                if self.amount > 0:
                    self.amount = -1 * self.amount

    def update(self, vert_dir=""):
        self.player_input()

        # Auto movement
        self.movement()

        # Go up or down by x amount
        if vert_dir != "":
            self.follow_ball = True
            # print("vert_dir: " + vert_dir)

        # Follow player aka predict roughly where ball will come
        if vert_dir == "up":
            # print("Player hit the ball UP")
            self.ball_direction = "up"
            self.amount = -1 * choice(speed_choices)
        elif vert_dir == "down":
            # print("Player hit the ball DOWN")
            self.ball_direction = "down"
            self.amount = choice(speed_choices)

        # if not self.follow_ball:
        # self.rect.y += self.amount

        # Dictate ball direction
        if self.amount:
            self.direction = "down"
        else:
            self.direction = "up"

        if self.follow_ball:
            # only go up or down by x amount until you hit a certain y-value
            self.rect.y += self.amount
            if vert_dir != "":
                if vert_dir == "up":
                    # go up
                    self.limit = randint(0, h / 4)  # 0 to 120

                elif vert_dir == "down":
                    # go down
                    self.limit = randint(h * 0.75, h)  # 360 to 480

                # print("limit: " + str(self.limit))
                # print("top: " + str(self.rect.top))
                # print("bottom: " + str(self.rect.bottom))

            if self.ball_direction == "up":
                if self.rect.top <= self.limit:
                    self.rect.top = self.limit
            elif self.ball_direction == "down":
                if self.rect.bottom >= self.limit:
                    self.rect.bottom = self.limit
