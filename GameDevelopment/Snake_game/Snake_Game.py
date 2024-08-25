
import pygame
import random
import os
pygame.init()
pygame.mixer.init()
width = 1000
height = 500
fps = 30
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Roboto", 32)
bg_img = pygame.image.load("green-snake-on-white-background-vector-26956864.jpg")
bg_img = pygame.transform.scale(bg_img, (width, height)).convert_alpha()

green = "#277a1d"
white = "#FFFFFF"
snake_colour = "#111210"
food_colour = (255, 0, 0)
txt_colour = "#202024"


def screen_text(text, color, pos_x, pos_y):
    screen = font.render(text, True, color)
    win.blit(screen, [pos_x, pos_y])


def plot_snake(window, color, pos_list, size):
    for x, y in pos_list:
        pygame.draw.rect(window, color, [x, y, size, size])


def welcome():
    exit_game = False
    while not exit_game:
        win.fill(white)
        screen_text("Welcome to GRD Snakes!", txt_colour, 250, 200)
        screen_text("Click SpaceBar to Start the game!", txt_colour, 250, 250)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit_game = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    snake_loop()
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


def snake_loop():
    with open('highscore.txt', 'r') as f:
        high_score = f.read()
    snk_lst = []
    snk_len = 1
    exit_game = False
    game_over = False
    snake_i_pox_x = 45
    snake_i_pox_y = 55
    snake_size = 15
    snake_vel_x = 0
    snake_init_vel = 2
    snake_vel_y = 0
    x_food = random.randint(20, width / 2)
    y_food = random.randint(20, height / 2)
    score = 0

    while not exit_game:
        if game_over:
            with open('highscore.txt', 'w') as f:
                f.write(str(high_score))
            win.fill(white)
            screen_text("Press enter to Restart Game", txt_colour, 250, 250)
            screen_text("Score  " + str(score), txt_colour, 250, 200)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit_game = True

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        snake_loop()
                    if e.key == pygame.K_ESCAPE:
                        welcome()
        else:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit_game = True
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RIGHT:
                        snake_vel_x = snake_init_vel
                        snake_vel_y = 0
                    elif e.key == pygame.K_LEFT:
                        snake_vel_x = -snake_init_vel
                        snake_vel_y = 0
                    elif e.key == pygame.K_UP:
                        snake_vel_y = -snake_init_vel
                        snake_vel_x = 0
                    elif e.key == pygame.K_DOWN:
                        snake_vel_y = snake_init_vel
                        snake_vel_x = 0
                    if e.key == pygame.K_ESCAPE:
                        welcome()
            snake_i_pox_x = snake_i_pox_x + snake_vel_x
            snake_i_pox_y = snake_i_pox_y + snake_vel_y
            if abs(snake_i_pox_x - x_food) < 6 and abs(snake_i_pox_y - y_food) < 6:
                score += 10
                x_food = random.randint(20, width / 2)
                y_food = random.randint(20, height / 2)
                snake_init_vel += 0.5
                snk_len += 2
                if score > int(high_score):
                    high_score = score
            head = [snake_i_pox_x, snake_i_pox_y]
            snk_lst.append(head)
            win.fill(green)
            win.blit(bg_img, (0, 0))
            screen_text("Score:" + str(score) + "  HighScore:" + str(high_score), txt_colour, 0, 0)
            pygame.draw.rect(win, food_colour, [x_food, y_food, snake_size, snake_size])
            if len(snk_lst) > snk_len:
                del snk_lst[0]
            if snake_i_pox_x < 0 or snake_i_pox_x > width or snake_i_pox_y < 0 or snake_i_pox_y > height:
                game_over = True
            if head in snk_lst[:-1]:
                game_over = True
            plot_snake(win, snake_colour, snk_lst, snake_size)
            pygame.draw.rect(win, snake_colour, [snake_i_pox_x, snake_i_pox_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome()
