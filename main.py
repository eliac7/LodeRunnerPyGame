import pygame
from pygame.locals import *
import random
from src.block import Block
from src.player import Player
from src.platform import Platform
from src.levels import Level, Level_01
from src.ladder import Ladder
from src.Enemy import Enemy
import math

# colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


def main():
    """ Main Program """
    pygame.time.set_timer(USEREVENT + 1, 1000)
    pygame.time.set_timer(USEREVENT + 2, 1000)
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    pygame.mixer.init()
    bg_sound = pygame.mixer.Sound("src/sound/bg.wav")

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Lode Runner")

    # Create the player
    player = Player()
    player_list = pygame.sprite.Group()
    player_list.add(player)

    # Create all the levels
    level_list = [Level_01(player)]

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    block_list = pygame.sprite.Group()
    player.level = current_level

    # Enemy

    enemy_list = pygame.sprite.Group()
    enemy = Enemy(5, 64, 64, current_level.get_platform_list(), current_level.get_levels())
    enemy_list.add(enemy)
    enemy = Enemy(3, 64, 64, current_level.get_platform_list(), current_level.get_levels())
    enemy_list.add(enemy)
    enemy = Enemy(1, 64, 64, current_level.get_platform_list(), current_level.get_levels())
    enemy_list.add(enemy)
    enemy = Enemy(0, 64, 64, current_level.get_platform_list(), current_level.get_levels())
    enemy_list.add(enemy)
    enemy = Enemy(6, 64, 64, current_level.get_platform_list(), current_level.get_levels())
    enemy_list.add(enemy)

    # arxikopoihsh tou player
    player.rect.x = 500
    player.rect.y = 490
    all_sprites_list = pygame.sprite.Group()
    # ladder
    ladder_list = pygame.sprite.Group()
    for i in range(10):
        ladder = Ladder(210, 410 - (20 * (i + 1)), 'src/ladder.png')  # 1
        ladder_list.add(ladder)
    for i in range(7):
        ladder = Ladder(610, 215 - (20 * (i + 1)), 'src/ladder.png')  # 2
        ladder_list.add(ladder)
    for i in range(11):
        ladder = Ladder(790, 570 - (20 * (i + 1)), 'src/ladder.png')  # 3
        ladder_list.add(ladder)
    for i in range(9):
        ladder = Ladder(2.5, 570 - (20 * (i + 1)), 'src/ladder.png')  # 4
        ladder_list.add(ladder)
        for i in range(8):
            ladder = Ladder(680, 360 - (20 * (i + 1)), 'src/ladder.png')  # 5
            ladder_list.add(ladder)

    # health

    heart = pygame.image.load('src/heart.png')

    # ladder_list.add(ladder1)
    # ladder_list.add(ladder2)
    # ladder_list.add(ladder3)
    # ladder_list.add(ladder4)

    for i in range(1):
        # This represents a block
        block = Block('src/coin.png')
        # music
        sound_coin = pygame.mixer.Sound("src/sound/coin.wav")
        oof = pygame.mixer.Sound("src/sound/oof.wav")
        oof.set_volume(0.6)

        # Set a random location for the block
        prev_level = random.randrange(0, 6)
        prev_level = block.new_coin(current_level.get_levels(), prev_level)
        while True:
            if pygame.sprite.spritecollide(block, ladder_list, False):
                prev_level = block.new_coin(current_level.get_levels(), prev_level)
            else:
                break
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
    font = pygame.font.Font('src/Pixel.otf', 20)
    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    FPS = 50
    score = 0
    removed_blocks = []
    health = 5
    last_time_hit = 0
    removed_enemies = []
    game_over = False
    bg_sound.play()
    bg = pygame.image.load("src/oof.jpg")
    # -------- Main Program Loop -----------
    while not done:

        if pygame.sprite.spritecollide(player, ladder_list, False):
            climbing = True
            player.set_is_climbing(True)
            player.setchangey(0)
        else:
            climbing = False
            player.setpressingbutton(False)

            player.set_is_climbing(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == USEREVENT + 1:
                for block in removed_blocks:
                    if block[1] >= 3:
                        replace_block = current_level.replace_block(block[0])
                        removed_blocks.remove(block)
                        hit_list = pygame.sprite.spritecollide(replace_block, enemy_list, False)
                        for enemies in hit_list:
                            enemies.set_vel(0)
                            removed_enemy = enemies.getID()
                            removed_enemies.append([removed_enemy, 0])
                            enemy_list.remove(enemies)
                        hit_list = pygame.sprite.spritecollide(replace_block, player_list, False)
                        for players in hit_list:
                            health = 0
                            player_list.remove(players)

                        platform_list = current_level.get_platform_list()
                        for enemies in enemy_list:
                            enemies.set_platform(platform_list)
                    else:
                        block[1] += 1
            if event.type == USEREVENT + 2:
                for enemies in removed_enemies:
                    enemies[1] += 1
                    if enemies[1] >= 10:
                        enemy = Enemy(enemies[0][0], enemies[0][1], enemies[0][2], enemies[0][3], enemies[0][4])
                        enemy_list.add(enemy)
                        removed_enemies.remove(enemies)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left(screen)
                if event.key == pygame.K_RIGHT:
                    player.go_right(screen)
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_UP and climbing == True:
                    player.climb(-3, True)
                if event.key == pygame.K_DOWN and climbing == True:
                    player.climb(3, True)
                if event.key == pygame.K_r:
                    block_for_remove = player.destroy_block(current_level)

                    if block_for_remove != 0:
                        removed_blocks.append([block_for_remove, 0])
                        current_level.remove_block(block_for_remove)

                    platform_list = current_level.get_platform_list()
                    for enemies in enemy_list:
                        enemies.set_platform(platform_list)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.climb(0, False)
                if event.key == pygame.K_DOWN:
                    player.climb(0, False)

                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)

        # Check the list of collisions.
        for block in blocks_hit_list:
            score += 1
            sound_coin.play()
            prev_level = block.new_coin(current_level.get_levels(), prev_level)
            while True:
                if pygame.sprite.spritecollide(block, ladder_list, False):
                    prev_level = block.new_coin(current_level.get_levels(), prev_level)
                else:
                    break
        for players in player_list:
            if pygame.time.get_ticks() > last_time_hit + 3000 or last_time_hit == 0:
                if pygame.sprite.spritecollide(players, enemy_list, False):
                    health -= 1
                    oof.play()
                    last_time_hit = pygame.time.get_ticks()
                    if health == 0:
                        player_list.remove(players)

        # health
        for i in range(health):
            screen.blit(heart, [850 + (i * 30), 30])

        # Draw all the sprites
        # Update the player.
        if game_over:
            FPS = 0
            show_go_screen(screen, clock, bg_sound, bg, score)
            game_over = False
            main()
        for enemies in enemy_list:
            enemies.draw(screen)
        player_list.update(screen)
        player_list.draw(screen)
        current_level.draw(screen)
        all_sprites_list.draw(screen)
        ladder_list.draw(screen)
        text2 = font.render("Score:   " + str(score), True, WHITE)
        screen.blit(text2, [850, 0])
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        if health == 0:
            game_over = True
        # Limit to 50 frames per second
        clock.tick(FPS)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


def show_go_screen(screen, clock, bg_sound, bg, score):
    screen.blit(bg, (0, 0))
    bg_sound.stop()
    fail = pygame.mixer.Sound("src/sound/fail.wav")
    fail.set_volume(.2)
    fail.play()
    font = pygame.font.Font('src/Pixel.otf',50)
    font2 = pygame.font.Font('src/Pixel.otf', 30)
    text = font.render(" YOU    LOST ", True, WHITE)
    screen.blit(text, [300, 260])
    text3 = font2.render("Score:  " + str(score), True, WHITE)
    screen.blit(text3, [370, 360])
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


if __name__ == "__main__":
    main()
