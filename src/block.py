import pygame
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

coin = [pygame.image.load('src/coin/coin1.png'),
        pygame.image.load('src/coin/coin2.png'),
        pygame.image.load('src/coin/coin3.png'),
        pygame.image.load('src/coin/coin4.png'),
        pygame.image.load('src/coin/coin5.png'),
        pygame.image.load('src/coin/coin6.png')]


class Block(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.rotate = 0

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def new_coin(self, level, prev_level):

        while True:
            y = random.randrange(0, 7)
            if y != prev_level:
                prev_level = y
                break
        matrix = []
        for i in range(len(level)):
            if (level[i][4]) == prev_level:
                matrix.append(level[i])
        xstart = 5000
        xend = -1
        for i in matrix:
            if (i[2]) < xstart:
                xstart = i[2]
                if xend == -1:
                    xend = i[2] + i[0]
            elif i[2] > xend:
                xend = i[2] + i[0]
        new_pos = random.randrange(xstart, xend - 50)
        self.rect.x = new_pos
        self.rect.y = matrix[0][3] - matrix[0][1]
        return prev_level

    def update(self, screen):
        if self.rotate >= 6:
            self.rotate = 0
        screen.blit(coin[int(self.rotate) // 1], (self.rect.x, self.rect.y))
        self.rotate += 0.25
