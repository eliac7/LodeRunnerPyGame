import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
global left
global right
global walkCount
left = False
right = False
walkCount = 0

walkRight = [pygame.image.load('src/Game/R1.png'), pygame.image.load('src/Game/R2.png'),
             pygame.image.load('src/Game/R3.png'),
             pygame.image.load('src/Game/R4.png'), pygame.image.load('src/Game/R5.png'),
             pygame.image.load('src/Game/R6.png'),
             pygame.image.load('src/Game/R7.png'), pygame.image.load('src/Game/R8.png'),
             pygame.image.load('src/Game/R9.png')]
walkLeft = [pygame.image.load('src/Game/L1.png'), pygame.image.load('src/Game/L2.png'),
            pygame.image.load('src/Game/L3.png'),
            pygame.image.load('src/Game/L4.png'), pygame.image.load('src/Game/L5.png'),
            pygame.image.load('src/Game/L6.png'),
            pygame.image.load('src/Game/L7.png'), pygame.image.load('src/Game/L8.png'),
            pygame.image.load('src/Game/L9.png')]


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load('src/Game/standing.png')
        pygame.display.flip()

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

        self.isclimbing = False

        self.pressingbutton = False

        self.looking = False

    def update(self, screen):
        global walkCount
        """ Move the player. """
        # Gravity

        # Climb
        if not self.isclimbing:
            # Gravity
            self.calc_grav()
        # Move left/right
        self.rect.x += self.change_x
        # moving picture
        if self.change_x == -6:

            if walkCount + 1 >= 27:
                walkCount = 0
            screen.blit(walkLeft[walkCount // 3], (self.rect.x, self.rect.y))
            walkCount += 1
        elif self.change_x == 6:

            if walkCount + 1 >= 27:
                walkCount = 0
            screen.blit(walkRight[walkCount // 3], (self.rect.x, self.rect.y))

            walkCount += 1
        elif self.change_x == 0:
            screen.blit(pygame.image.load('src/Game/standing.png'), (self.rect.x, self.rect.y))
        pygame.display.update()

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .65

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -9

    # Player-controlled movement:
    def go_left(self, screen):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.looking = True

    def go_right(self, screen):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.looking = False

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def climb(self, change_y, pressingbutton):
        self.change_y = change_y
        self.isclimbing = True
        self.pressingbutton = pressingbutton

    def set_is_climbing(self, isclimbing):
        self.isclimbing = isclimbing

    def setchangey(self, y):
        if not self.pressingbutton:
            self.change_y = y

    def setpressingbutton(self, pressingbutton):
        self.pressingbutton = pressingbutton

    def destroy_block(self, level):
        blocks = level.get_levels()
        current_block = []
        for block in blocks:
            if block[2] < self.rect.x < block[2] + 36:
                if block[3] < self.rect.y + 63 < block[3] + 36:
                    current_block = block
        if len(current_block) != 0:
            if self.looking:  # lright
                try:
                    blocks.index(
                        [current_block[0], current_block[1], current_block[2] - 36, current_block[3], current_block[4]])
                    i = blocks.index(
                        [current_block[0], current_block[1], current_block[2] - 36, current_block[3], current_block[4]])
                    return blocks[i]
                except:
                    return 0


            elif not self.looking:  # left
                try:
                    blocks.index(
                        [current_block[0], current_block[1], current_block[2] + 36, current_block[3], current_block[4]])
                    i = blocks.index(
                        [current_block[0], current_block[1], current_block[2] + 36, current_block[3], current_block[4]])
                    return blocks[i]
                except:
                    return 0
        else:
            return 0

    def get_X(self):
        return self.rect.x

    def get_Y(self):
        return self.rect.y
