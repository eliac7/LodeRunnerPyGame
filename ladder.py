import pygame


class Ladder(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = height
        self.x = width
        self.y = height

    def updateImage(self, width, height):
        self.image = pygame.image.load('src/ladder_1.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
