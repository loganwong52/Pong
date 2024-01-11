# python imports
import pygame
from sys import exit
from random import randint, choice

# local imports
from player import Player
from opponent import Opponent
from ball import Ball

pygame.init()
# CREATE DISPLAY SURFACE
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Pong")
game_active = True

# Create the clock object for the framerate
clock = pygame.time.Clock()

# Timer for enemy
# opponent_timer = pygame.USEREVENT + 1
# pygame.time.set_timer(opponent_timer, 3000)

# Player score
score = 0

# Group single
player = pygame.sprite.GroupSingle()
player.add(Player())

opponent = pygame.sprite.GroupSingle()
opponent.add(Opponent())

ball = pygame.sprite.Group()
ball.add(Ball())

# While loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")
    # screen.blit(background, (0, 0))

    player.draw(screen)
    player.update()

    opponent.draw(screen)
    opponent.update()

    ball.draw(screen)
    ball.update()

    # Update everything
    pygame.display.update()
    clock.tick(60)
