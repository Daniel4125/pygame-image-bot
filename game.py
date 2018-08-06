import pygame
from pygame.locals import *

pygame.init()
game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('pygame')
clock = pygame.time.Clock()

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    game_display.fill(WHITE)
    pygame.draw.circle(game_display, BLUE, (300, 50), 20, 0)
    pygame.display.update()
    clock.tick(60)
pygame.quit()

quit()


