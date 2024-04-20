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
BODY_VERTICAL = pygame.image.load(os.path.join('assets', 'body_vertical.png'))

# def update_body():
#     if len(snake_body) > 0:
#         for i in range(len(snake_body) -1, 0, -1):
#             snake_body[i].x = snake_body[i - 1].x
#             snake_body[i].y = snake_body[i - 1].y
        
#         snake_body[0].x = (player_head.x + 20)
#         snake_body[0].y = (player_head.y + 20)

class Snake:
    def __init__(self):
        self.head = pygame.Rect((constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, 20, 20))
        self.body = []
        self.body.append(self.head)

    def move(self, dx, dy):
        self.head.move_ip(dx, dy)
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1].copy()

    def grow(self):
        last_segment = self.body[-1]
        new_segment = pygame.Rect(last_segment.x, last_segment.y, 20, 20)
        self.body.append(new_segment)

    def draw(self, surface, head_direction):
        for i, segment in enumerate(self.body):
            if i == 0:
                continue
            surface.blit(BODY_VERTICAL, segment)

        surface.blit(head_direction, self.head)


def main():
    IN_GAME = True

    hebi = Snake()

    food = pygame.Rect((random.randint(0, 40) * constants.TILESIZE, random.randint(0, 30) * constants.TILESIZE, 20, 20))
    head_direction = HEAD_DOWN

    while IN_GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IN_GAME = False

        offsetX, offsetY = screen.get_size()
        screen.fill((constants.BLACK))

        hebi.draw(screen, head_direction)
        screen.blit(APPLE, (food.x, food.y))

        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True and hebi.head.left > 0:
            head_direction = HEAD_LEFT
            hebi.move(-constants.TILESIZE, 0)
        elif key[pygame.K_d] == True and hebi.head.right < offsetX:
            head_direction = HEAD_RIGHT
            hebi.move(constants.TILESIZE, 0)
        elif key[pygame.K_w] == True and hebi.head.top > 0:
            head_direction = HEAD_UP
            hebi.move(0, -constants.TILESIZE)
        elif key[pygame.K_s] == True and hebi.head.bottom < offsetY:
            head_direction = HEAD_DOWN
            hebi.move(0, constants.TILESIZE)

        eat = pygame.Rect.colliderect(hebi.head, food)

        if eat:
            food.x = random.randint(0, 40) * constants.TILESIZE
            food.y = random.randint(0, 30) * constants.TILESIZE
            hebi.grow()

        pygame.display.flip()
        clock.tick(16) #Limit 10 FPS for smoother movements

    pygame.quit()

if __name__ == "__main__":
    main()