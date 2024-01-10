# python imports
import pygame
from sys import exit
from random import randint, choice

pygame.init()
# CREATE DISPLAY SURFACE
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pong")

# Create the clock object for the framerate
clock = pygame.time.Clock()

# While loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update everything
    pygame.display.update()
    clock.tick(60)
