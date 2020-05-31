import pygame
from pygame.locals import *
import random
from src.block import Block
from src.player import Player
from src.platform import Platform
from src.levels import Level, Level_01, Level_02
from src.ladder import Ladder
from src.Enemy import Enemy
from src.button import Button
from src.cursor import Cursor
import time

# colors

global play_intro_music
play_intro_music = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


def main():
    global play_intro_music
    """ Main Program """
    pygame.time.set_timer(USEREVENT + 1, 1000)
    pygame.time.set_timer(USEREVENT + 2, 1000)

    # Sound

    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    pygame.mixer.init()
    bg_sound = pygame.mixer.Sound("src/sound/bg.wav")
    welcome_music = pygame.mixer.Sound("src/sound/welcome.wav")
    sound_coin = pygame.mixer.Sound("src/sound/coin.wav")
    oof = pygame.mixer.Sound("src/sound/oof.wav")
    oof.set_volume(0.6)

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Lode Runner")

    # health

    heart = pygame.image.load('src/heart.png')

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
    game_over = True
    start_game = True
    bg = pygame.image.load("src/oof.jpg")
    welcome_bg = pygame.image.load("src/welcome_bg.jpg")
    help = pygame.image.load('src/how_to.jpg')
    # -------- Main Program Loop -----------
    while not done:
        if game_over:
            if start_game:
                choice = start_game_screen(screen, clock, welcome_music, welcome_bg, help)
                start_game = False

                game_over = False
                score = 0
                removed_blocks = []
                health = 5
                last_time_hit = 0
                removed_enemies = []
                # restart  game

                # player
                if choice == 1:
                    # Create the player
                    bg_sound.play()
                    player = Player()
                    player_list = pygame.sprite.Group()
                    player_list.add(player)

                    # Create all the levels
                    level_list = [Level_01(player, 'src/brick_2.jpg')]

                    # Set the current level
                    current_level_no = 0
                    current_level = level_list[current_level_no]

                    player.level = current_level

                    # initialize player
                    player.rect.x = 500
                    player.rect.y = 490
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

                    # enemy
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

                    # coins
                    for i in range(1):
                        #  This represents a block
                        block = Block('src/coin.png')
                    block_list = pygame.sprite.Group()
                    all_sprites_list = pygame.sprite.Group()
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
                elif choice == 2:
                    # Create the player
                    bg_sound.play()
                    player = Player()
                    player_list = pygame.sprite.Group()
                    player_list.add(player)

                    # Create all the levels
                    level_list = [Level_02(player, 'src/brick_purple.jpg')]

                    # Set the current level
                    current_level_no = 0
                    current_level = level_list[current_level_no]

                    player.level = current_level

                    # initialize player
                    player.rect.x = 500
                    player.rect.y = 490
                    # ladder
                    ladder_list = pygame.sprite.Group()
                    for i in range(25):
                        ladder = Ladder(180, 570 - (20 * (i + 1)), 'src/ladder.png')  # 1
                        ladder_list.add(ladder)
                    for i in range(25):
                        ladder = Ladder(770, 570 - (20 * (i + 1)), 'src/ladder.png')  # 2
                        ladder_list.add(ladder)

                    # enemy
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
                    # blocks
                    for i in range(1):
                        #  This represents a block
                        block = Block('src/coin.png')
                    block_list = pygame.sprite.Group()
                    all_sprites_list = pygame.sprite.Group()
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
                elif choice == -1:
                    done = True
                elif choice == 3:
                    return_button = Button('src/return_white.png', 930, 20, 10)
                    button_list = pygame.sprite.Group()
                    button_list.add(return_button)
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    cursor_list = pygame.sprite.Group()
                    cursor = Cursor('src/cursor.png', x, y)
                    cursor_list.add(cursor)

            else:
                if choice == 1:
                    choice = show_go_screen(screen, clock, bg_sound, 'src/oof.jpg', score, choice)
                elif choice == 2:
                    choice = show_go_screen(screen, clock, bg_sound, 'src/oof_level02.jpg', score, choice)
                start_game = True
        if choice != -1 and choice != 3:
            screen.fill(BLACK)
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
                if choice == 1:
                    screen.blit(heart, [850 + (i * 30), 30])
                elif choice == 2:
                    screen.blit(heart, [437 + (i * 30), 30])

            # Draw all the sprites
            # Update the player.

            text2 = font.render("Score:   " + str(score), True, WHITE)
            if choice == 1:
                screen.blit(text2, [850, 0])
            elif choice == 2:
                screen.blit(text2, [450, 0])
            current_level.draw(screen)
            block_list.update(screen)
            ladder_list.draw(screen)
            player_list.update(screen)
            for enemies in enemy_list:
                enemies.movement(screen)

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
            if health == 0:
                game_over = True
        elif choice == 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.spritecollide(cursor, button_list, False):
                    buttons = pygame.sprite.spritecollide(cursor, button_list, False)
                    for button in buttons:
                        level = button.selected()
                        if level == 10:
                            start_game = True
                            game_over = True
                            play_intro_music = False
            image = pygame.image.load('src/how_to.jpg')
            screen.blit(image, (0, 0))
            isOverOut = False
            for button in pygame.sprite.spritecollide(cursor, button_list, False):
                isOverOut = True
                level = button.selected()
                if level == 10:
                    button.isOver('src/return.png')
            if not isOverOut:
                for button in button_list:
                    level = button.selected()
                    if level == 10:
                        button.isOver('src/return_white.png')
            button_list.draw(screen)
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            cursor.update(x, y)
            cursor_list.draw(screen)

            # Limit to 50 frames per second
        clock.tick(FPS)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    pygame.quit()


def show_go_screen(screen, clock, bg_sound, bg, score, choice):
    bg = pygame.image.load(bg)
    screen.blit(bg, (0, 0))
    bg_sound.stop()
    fail = pygame.mixer.Sound("src/sound/fail.wav")
    fail.set_volume(.2)
    fail.play()
    font = pygame.font.Font('src/Pixel.otf', 50)
    font2 = pygame.font.Font('src/Pixel.otf', 30)
    if choice == 1:
        text = font.render(" YOU    LOST ", True, WHITE)
        screen.blit(text, [300, 260])
        text3 = font2.render("Score:  " + str(score), True, WHITE)
        screen.blit(text3, [370, 360])
        font3 = pygame.font.Font('src/Pixel.otf', 15)
        text4 = font3.render("Press any key to play again", True, WHITE)
        screen.blit(text4, [320, 460])
    else:
        text = font.render(" YOU    LOST ", True, WHITE)
        screen.blit(text, [340, 260])
        text3 = font2.render("Score:  " + str(score), True, WHITE)
        screen.blit(text3, [420, 370])
        font3 = pygame.font.Font('src/Pixel.otf', 15)
        text4 = font3.render("Press any key to play again", True, WHITE)
        screen.blit(text4, [370, 460])
    pygame.display.flip()
    waiting = True
    while waiting:
        time.sleep(1)
        clock.tick(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
                waiting = False
            if event.type == pygame.KEYUP:
                waiting = False
                fail.stop()

    return 0


def start_game_screen(screen, clock, welcome_music, welcome_bg, help):
    global play_intro_music
    pygame.mouse.set_visible(False)
    button_list = pygame.sprite.Group()
    button = Button('src/level01_gray.jpg', 280, 250, 1)
    button_list.add(button)
    button = Button('src/level02_gray.jpg', 550, 250, 2)
    button_list.add(button)
    button = Button('src/help.png', 930, 20, 3)
    button_list.add(button)

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    cursor_list = pygame.sprite.Group()
    cursor = Cursor('src/cursor.png', x, y)
    cursor_list.add(cursor)
    welcome_music.set_volume(.5)
    if play_intro_music:
        welcome_music.play()
    pygame.display.flip()
    waiting = True
    isOverOut = False
    while waiting:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        cursor.update(x, y)
        clock.tick(60)
        isOverOut = False
        for button in pygame.sprite.spritecollide(cursor, button_list, False):
            isOverOut = True
            level = button.selected()
            if level == 1:
                button.isOver('src/level01_color.jpg')
            elif level == 2:
                button.isOver('src/level02_color.jpg')
            else:
                button.isOver('src/help_over.png')
        if not isOverOut:
            for button in button_list:
                level = button.selected()
                if level == 1:
                    button.isOver('src/level01_gray.jpg')
                elif level == 2:
                    button.isOver('src/level02_gray.jpg')
                else:
                    button.isOver('src/help.png')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choice = -1
                waiting = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.spritecollide(cursor, button_list, False):
                buttons = pygame.sprite.spritecollide(cursor, button_list, False)
                for button in buttons:
                    choice = button.selected()
                    if choice == 1:
                        play_intro_music = True
                        waiting = False
                        welcome_music.stop()
                    elif choice == 2:
                        play_intro_music = True
                        waiting = False
                        welcome_music.stop()
                    elif choice == 3:
                        waiting = False

        screen.blit(welcome_bg, (0, 0))
        button_list.draw(screen)
        cursor_list.draw(screen)
        pygame.display.flip()
    return choice


if __name__ == "__main__":
    main()
