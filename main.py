import pygame, sys, os
from pygame.locals import *
import constants
import random

pygame.init()

# Global scope variables
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
icon = pygame.image.load('redblazer.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Hebi Game')
clock = pygame.time.Clock()

#assets from opengameart.org
APPLE = pygame.image.load(os.path.join('assets', 'apple.png'))
HEAD_UP = pygame.image.load(os.path.join('assets', 'head_up.png'))
HEAD_DOWN = pygame.image.load(os.path.join('assets', 'head_down.png'))
HEAD_RIGHT = pygame.image.load(os.path.join('assets', 'head_right.png'))
HEAD_LEFT = pygame.image.load(os.path.join('assets', 'head_left.png'))


player = pygame.Rect((constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, 20, 20))

class Hebi:
    def __init__(self):
        self.length = 1
        self.position = ((constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2))

def main():
    IN_GAME = True

    food = pygame.Rect((random.randint(0, 40) * constants.TILESIZE, random.randint(0, 30) * constants.TILESIZE, 20, 20))
    head_direction = HEAD_DOWN

    while IN_GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IN_GAME = False

        offsetX, offsetY = screen.get_size()
        screen.fill((constants.BLACK))
        screen.blit(head_direction, (player.x, player.y))
        screen.blit(APPLE, (food.x, food.y))

        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True and player.left > 0:
            head_direction = HEAD_LEFT
            player.move_ip(-constants.TILESIZE, 0)
        elif key[pygame.K_d] == True and player.right < offsetX:
            head_direction = HEAD_RIGHT
            player.move_ip(constants.TILESIZE, 0)
        elif key[pygame.K_w] == True and player.top > 0:
            head_direction = HEAD_UP
            player.move_ip(0, -constants.TILESIZE)
        elif key[pygame.K_s] == True and player.bottom < offsetY:
            head_direction = HEAD_DOWN
            player.move_ip(0, constants.TILESIZE)

        eat = pygame.Rect.colliderect(player, food)

        if eat:
            food.x = random.randint(0, 40) * constants.TILESIZE
            food.y = random.randint(0, 30) * constants.TILESIZE

        pygame.display.flip()
        clock.tick(16) #Limit 10 FPS for smoother movements

    pygame.quit()

if __name__ == "__main__":
    main()