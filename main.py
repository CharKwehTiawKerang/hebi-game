import pygame, sys
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
IN_GAME = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
icon = pygame.image.load('redblazer.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Hebi Game')

player = pygame.Rect((300, 250, 25, 25))

while IN_GAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IN_GAME = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    pygame.display.update()

pygame.quit()