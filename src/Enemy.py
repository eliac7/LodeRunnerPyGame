import pygame

global walkRight
global walkLeft
global walkCount

walkCount = 0
# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

walkRight = [pygame.image.load('src/Game/enemy/R1E.png'), pygame.image.load('src/Game/enemy/R2E.png'),
             pygame.image.load('src/Game/enemy/R3E.png'),
             pygame.image.load('src/Game/enemy/R4E.png'), pygame.image.load('src/Game/enemy/R5E.png'),
             pygame.image.load('src/Game/enemy/R6E.png'),
             pygame.image.load('src/Game/enemy/R7E.png'), pygame.image.load('src/Game/enemy/R8E.png'),
             pygame.image.load('src/Game/enemy/R9E.png'), pygame.image.load('src/Game/enemy/R10E.png'),
             pygame.image.load('src/Game/enemy/R11E.png')]

walkLeft = [pygame.image.load('src/Game/enemy/L1E.png'), pygame.image.load('src/Game/enemy/L2E.png'),
            pygame.image.load('src/Game/enemy/L3E.png'),
            pygame.image.load('src/Game/enemy/L4E.png'), pygame.image.load('src/Game/enemy/L5E.png'),
            pygame.image.load('src/Game/enemy/L6E.png'),
            pygame.image.load('src/Game/enemy/L7E.png'), pygame.image.load('src/Game/enemy/L8E.png'),
            pygame.image.load('src/Game/enemy/L9E.png'), pygame.image.load('src/Game/enemy/L10E.png'),
            pygame.image.load('src/Game/enemy/L11E.png')]


class Enemy(pygame.sprite.Sprite):

    def __init__(self, platform, width, height, platform_list, level):
        super().__init__()
        self.platform = platform
        self.platform_list = platform_list
        self.level = level
        matrix = []
        for i in range(len(level)):
            if (level[i][4]) == platform:
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
        y = matrix[0][3] - 15
        self.image = pygame.image.load('src/Game/enemy/L1E.png')
        self.rect = self.image.get_rect()
        self.rect.x = xstart+50
        self.rect.y = y
        self.width = width
        self.height = height
        self.path = [xstart, xend - 30]  # This will define where our enemy starts and finishes their path.
        self.platform_height = y + 54
        self.walkCount = 0
        self.vel = 3
        self.vel_y = 0
        self.isDropping = False


    def draw(self, screen):
        global walkCount
#        if  self.isDropping == True :
            # Gravity
        self.calc_grav()
        self.move()

        if walkCount + 1 >= 33:  # Since we have 11 images for each animtion our upper bound is 33.
            # We will show each image for 3 frames. 3 x 11 = 33.
            walkCount = 0

        if self.vel > 0:  # If we are moving to the right we will display our walkRight images
            screen.blit(walkRight[walkCount // 3], (self.rect.x, self.rect.y))
            walkCount += 1
            pygame.display.update()

        else:  # Otherwise we will display the walkLeft images
            screen.blit(walkLeft[walkCount // 3], (self.rect.x, self.rect.y))
            walkCount += 1
            pygame.display.update()
        block_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit6
            if self.vel > 0:
                self.rect.right = block.rect.left
            elif self.vel < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        self.rect.y += self.vel_y
        block_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.vel_y > 0:
                self.rect.bottom = block.rect.top
            elif self.vel_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.vel_y = 0

    def move(self):

        if self.vel > 0:  # If we are moving right
            if self.rect.x < self.path[1] + self.vel:  # If we have not reached the furthest right point on our path.
                self.rect.x += self.vel
            else:  # Change direction and move back the other way
                self.vel = self.vel * -1
                self.rect.x += self.vel
                # walkCount = 0
        else:  # If we are moving left
            if self.rect.x > self.path[0] - self.vel:  # If we have not reached the furthest left point on our path
                self.rect.x += self.vel
            else:  # Change direction
                self.vel = self.vel * -1
                self.rect.x += self.vel
                # walkCount = 0

    def get_X(self):
        return self.rect.x

    def get_Y(self):
        return self.rect.y


    def calc_grav(self):
        self.isDropping = True
        """ Calculate effect of gravity. """
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            self.vel_y += .65

        # See if we are on the ground.
        if self.rect.y >= self.platform_height - self.rect.height and self.vel_y >= 0:
            self.isDropping = False
            self.vel_y = 0
            self.rect.y = self.platform_height - self.rect.height

    def set_platform(self, platform_list):
        self.platform_list= platform_list

    def set_vel(self,vel):
        self.vel = vel
    def getID(self):
        return [self.platform,self.width,self.height,self.platform_list,self.level]