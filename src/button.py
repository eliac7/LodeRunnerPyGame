import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, image, x, y, level_name):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.level_name = level_name

    def isOver(self, image):
        self.image = pygame.image.load(image)

    def selected(self):
        return self.level_name
