import pygame


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load('src/brick_2.jpg')

        self.rect = self.image.get_rect()

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y
