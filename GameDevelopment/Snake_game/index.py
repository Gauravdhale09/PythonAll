import pygame
import random
import os

pygame.init()
pygame.mixer.init()


class Snake:
    def __init__(self):
        self.sc_width = 1000
        self.sc_height = 500
        self.sc_fps = 30
        self.window = pygame.display.set_mode((self.sc_width, self.sc_height))
        pygame.display.set_caption("Snake-Arena")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Roboto", 32)
        self.exit = False
        self.white = "#FFFFFF"
        self.black = "#000000"

        self.snake_pos_x = 45
        self.snake_pos_y = 55
        self.snake_vel_x = 0
        self.snake_vel_y = 0
    def screen_text(self, text, color, pos_x, pos_y, font):
        screen = font.render(text, True, color)
        self.window.blit(screen, [pos_x, pos_y])

    def high_sc_file(self):
        if not os.path.exists("Highscore.txt"):
            with open("Highscore.txt", 'r') as f:
                high_score = f.read()
            return high_score
        else:
            with open("Highscore.txt", 'r') as f:
                high_score = f.read()
            return high_score
    def welcome(self):

        while not self.exit:
            self.window.fill(self.white)
            self.screen_text("Welcome to GRD Snakes!", self.black, 250, 200, self.font)
            self.screen_text("Click SpaceBar to Start the game!", self.black, 250, 250, self.font)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.exit = True
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        self.start()
            pygame.display.update()
            self.clock.tick(self.sc_fps)

        pygame.quit()
        quit()

    def start(self):
        snk_lst = []
        snk_len = 1
        game_over = False
        score = 0
        snake_init_vel = 2
        snake_size = 15
        food_pos_x = random.randint(20, int(self.sc_width) // 2)
        food_pos_y = random.randint(20, int(self.sc_height) // 2)
        while not self.exit:
            if game_over:
                self.window.fill(self.white)
                self.screen_text("Press enter to Restart Game", self.black, 250, 250, self.font)
                self.screen_text("Score  " + str(score), self.black, 250, 200, self.font)
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        self.exit = True

                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_RETURN:
                            self.start()
                        if e.key == pygame.K_ESCAPE:
                            self.welcome()
            else:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        self.exit = True
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_RIGHT:
                            self.snake_vel_x = snake_init_vel
                            self.snake_vel_y = 0
                        elif e.key == pygame.K_LEFT:
                            self.snake_vel_x = -snake_init_vel
                            self.snake_vel_y = 0
                        elif e.key == pygame.K_UP:
                            self.snake_vel_y = -snake_init_vel
                            self.snake_vel_x = 0
                        elif e.key == pygame.K_DOWN:
                            self.snake_vel_y = snake_init_vel
                            self.snake_vel_x = 0
                        if e.key == pygame.K_ESCAPE:
                            self.welcome()
                self.snake_pos_x += self.snake_vel_x
                self.snake_pos_y += self.snake_vel_y
                if abs(self.snake_pos_x - food_pos_x) < 6 and abs(self.snake_pos_y - food_pos_y) < 6:
                    score += 10
                    food_pos_x = random.randint(20, int(self.sc_width) // 2)
                    food_pos_y = random.randint(20, int(self.sc_height) // 2)
                    snake_init_vel += 5
                    snk_len += 2
                    high_score = self.high_sc_file()
                    if score > int(high_score):
                        high_score = score



if __name__ == '__main__':
    game = Snake()
    game.welcome()
