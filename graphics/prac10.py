import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 500))

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Draw hut
def draw_hut(screen):
    pygame.draw.line(screen, BLACK, (200, 150), (350, 150), 2)
    pygame.draw.line(screen, BLACK, (140, 200), (200, 150), 2)
    pygame.draw.line(screen, BLACK, (140, 330), (140, 200), 2)
    pygame.draw.line(screen, BLACK, (250, 200), (140, 200), 2)
    pygame.draw.line(screen, BLACK, (200, 150), (250, 200), 2)
    pygame.draw.circle(screen, BLACK, (196, 180), 15)
    pygame.draw.polygon(screen, GREEN, [(200, 150), (250, 200), (140, 200)])

# Draw door
def draw_door(screen):
    pygame.draw.line(screen, BLACK, (170, 260), (170, 330), 2)
    pygame.draw.line(screen, BLACK, (170, 260), (210, 260), 2)
    pygame.draw.polygon(screen, RED, [(170, 260), (210, 260), (180, 280)])

# Draw chimney
def draw_chimney(screen):
    pygame.draw.line(screen, BLACK, (290, 110), (290, 150), 2)
    pygame.draw.line(screen, BLACK, (310, 110), (310, 150), 2)
    pygame.draw.ellipse(screen, BLACK, (290, 100, 20, 50), 2)

# Draw window
def draw_window(screen):
    pygame.draw.line(screen, BLACK, (300, 250), (350, 250), 2)
    pygame.draw.line(screen, BLACK, (300, 280), (350, 280), 2)
    pygame.draw.line(screen, BLACK, (300, 250), (350, 280), 2)
    pygame.draw.line(screen, BLACK, (300, 280), (300, 250), 2)
    pygame.draw.line(screen, BLACK, (350, 280), (350, 250), 2)

# Animated text
def animated_text(screen, text, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, RED)
    screen.blit(text_surface, (x, y))

# Main loop
clock = pygame.time.Clock()
x = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    draw_hut(screen)
    draw_door(screen)
    draw_chimney(screen)
    draw_window(screen)
    pygame.draw.arc(screen, BLUE, (20, 290, 50, 50), 0.785, 0.928, 5)
    pygame.draw.line(screen, BLACK, (5, 330), (600, 330), 2)
    animated_text(screen, "Home Sweet Home", x, 390)
    x += 10
    if x > 800:
        x = 0
    pygame.display.update()
    clock.tick(60)