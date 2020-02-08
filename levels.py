import pygame
from src.platform import Platform

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.player = player

        # Background image
        self.background = None

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(BLACK)
        # screen=pygame.image.load('icon.jpg')
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        # Array with width, height, x, and y of platform
        self.level = [[36, 36, 0, 570, 0],  # katwkatw
                      [36, 36, 36, 570, 0],  # katwkatw
                      [36, 36, 72, 570, 0],  # katwkatw
                      [36, 36, 108, 570, 0],  # katwkatw
                      [36, 36, 144, 570, 0],  # katwkatw
                      [36, 36, 180, 570, 0],  # katwkatw
                      [36, 36, 216, 570, 0],  # katwkatw
                      [36, 36, 252, 570, 0],  # katwkatw
                      [36, 36, 288, 570, 0],  # katwkatw
                      [36, 36, 324, 570, 0],  # katwkatw
                      [36, 36, 360, 570, 0],  # katwkatw
                      [36, 36, 396, 570, 0],  # katwkatw
                      [36, 36, 432, 570, 0],  # katwkatw
                      [36, 36, 468, 570, 0],  # katwkatw
                      [36, 36, 504, 570, 0],  # katwkatw
                      [36, 36, 540, 570, 0],  # katwkatw
                      [36, 36, 576, 570, 0],  # katwkatw
                      [36, 36, 612, 570, 0],  # katwkatw
                      [36, 36, 648, 570, 0],  # katwkatw
                      [36, 36, 684, 570, 0],  # katwkatw
                      [36, 36, 720, 570, 0],  # katwkatw
                      [36, 36, 756, 570, 0],  # katwkatw
                      [36, 36, 792, 570, 0],  # katwkatw
                      [36, 36, 828, 570, 0],  # katwkatw
                      [36, 36, 864, 570, 0],  # katwkatw
                      [36, 36, 900, 570, 0],  # katwkatw
                      [36, 36, 936, 570, 0],  # katwkatw
                      [36, 36, 972, 570, 0],  # katwkatw
                      [36, 36, 840, 460, 1],  # katwdeksia
                      [36, 36, 876, 460, 1],  # katwdeksia
                      [36, 36, 912, 460, 1],  # katwdeksia
                      [36, 36, 948, 460, 1],  # katwdeksia
                      [36, 36, 984, 460, 1],  # katwdeksia
                      [36, 36, 580, 360, 2],  # mesaio
                      [36, 36, 616, 360, 2],  # mesaio
                      [36, 36, 652, 360, 2],  # mesaio
                      [36, 36, 688, 360, 2],  # mesaio
                      [36, 36, 724, 360, 2],  # mesaio
                      [36, 36, 755, 360, 2],  # mesaio
                      [36, 36, 55, 410, 3],  # karwaristera
                      [36, 36, 91, 410, 3],  # karwaristera
                      [36, 36, 127, 410, 3],  # karwaristera
                      [36, 36, 163, 410, 3],  # karwaristera
                      [36, 36, 199, 410, 3],  # karwaristera
                      [36, 36, 225, 410, 3],  # karwaristera
                      [36, 36, 0, 215, 4],  # mesaioaristera
                      [36, 36, 36, 215, 4],  # mesaioaristera
                      [36, 36, 72, 215, 4],  # mesaioaristera
                      [36, 36, 108, 215, 4],  # mesaioaristera
                      [36, 36, 144, 215, 4],  # mesaioaristera
                      [36, 36, 175, 215, 4],  # mesaioaristera
                      [36, 36, 260, 215, 5],  # panwmmesaio
                      [36, 36, 296, 215, 5],  # panwmmesaio
                      [36, 36, 332, 215, 5],  # panwmmesaio
                      [36, 36, 368, 215, 5],  # panwmmesaio
                      [36, 36, 404, 215, 5],  # panwmmesaio
                      [36, 36, 440, 215, 5],  # panwmmesaio
                      [36, 36, 476, 215, 5],  # panwmmesaio
                      [36, 36, 512, 215, 5],  # panwmmesaio
                      [36, 36, 548, 215, 5],  # panwmmesaio
                      [36, 36, 584, 215, 5],  # panwmmesaio
                      [36, 36, 620, 215, 5],  # panwmmesaio
                      [36, 36, 645, 215, 5],  # panwmmesaio
                      [36, 36, 0, 80, 6],  # panwpanw
                      [36, 36, 36, 80, 6],  # panwpanw
                      [36, 36, 72, 80, 6],  # panwpanw
                      [36, 36, 108, 80, 6],  # panwpanw
                      [36, 36, 144, 80, 6],  # panwpanw
                      [36, 36, 180, 80, 6],  # panwpanw
                      [36, 36, 216, 80, 6],  # panwpanw
                      [36, 36, 252, 80, 6],  # panwpanw
                      [36, 36, 288, 80, 6],  # panwpanw
                      [36, 36, 324, 80, 6],  # panwpanw
                      [36, 36, 360, 80, 6],  # panwpanw
                      [36, 36, 396, 80, 6],  # panwpanw
                      [36, 36, 432, 80, 6],  # panwpanw
                      [36, 36, 468, 80, 6],  # panwpanw
                      [36, 36, 504, 80, 6],  # panwpanw
                      [36, 36, 540, 80, 6],  # panwpanw
                      [36, 36, 576, 80, 6],  # panwpanw
                      ]

        # Go through the array above and add platforms

        for platform in self.level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

    def get_levels(self):
        return self.level

    def remove_block(self, block):
        for platforms in self.platform_list:
            if platforms.get_x() == block[2] and platforms.get_y() == block[3]:
                self.platform_list.remove(platforms)
                break

    def set_levels(self, new_level):
        self.level = new_level

    def replace_block(self, block):
        new_block = Platform(block[0], block[1])
        new_block.rect.x = block[2]
        new_block.rect.y = block[3]
        new_block.player = self.player
        self.platform_list.add(new_block)
        return new_block

    def get_platform_list(self):
        return self.platform_list
