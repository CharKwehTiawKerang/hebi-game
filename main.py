import pygame, sys
from pygame.locals import *
import constants
import random

pygame.init()

# Global scope variables
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), RESIZABLE)
icon = pygame.image.load('redblazer.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Hebi Game')
clock = pygame.time.Clock()

player = pygame.Rect((constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, 20, 20))
food = pygame.Rect((random.randint(0, 40) * constants.TILESIZE, random.randint(0, 30) * constants.TILESIZE, 20, 20))

class Hebi:
    def __init__(self):
        self.length = 1
        self.position = ((constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2))

def main():
    IN_GAME = True

    while IN_GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IN_GAME = False

        x, y = screen.get_size()
        screen.fill((constants.BLACK))
        pygame.draw.rect(screen, (255, 0, 0), player)
        pygame.draw.rect(screen, (200, 0, 100), food)

        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True and player.left > 0:
            player.move_ip(-constants.TILESIZE, 0)
        elif key[pygame.K_d] == True and player.right < constants.SCREEN_WIDTH:
            player.move_ip(constants.TILESIZE, 0)
        elif key[pygame.K_w] == True and player.top > 0:
            player.move_ip(0, -constants.TILESIZE)
        elif key[pygame.K_s] == True and player.bottom < constants.SCREEN_HEIGHT:
            player.move_ip(0, constants.TILESIZE)

        pygame.display.flip()
        clock.tick(16) #Limit 10 FPS for smoother movements

    pygame.quit()

if __name__ == "__main__":
    main()