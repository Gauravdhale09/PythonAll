import pygame
import math

# Initialize Pygame
pygame.init()

# Define window size and colors
window_size = (640, 480)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the display window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Set background color
screen.fill(WHITE)

# Function to implement DDA algorithm
def draw_dda(x0, y0, x1, y1):
    # Calculate dx and dy
    dx = x1 - x0
    dy = y1 - y0

    # Calculate the number of steps
    steps = max(abs(dx), abs(dy))

    # Calculate the increment for each step
    x_inc = dx / steps
    y_inc = dy / steps

    # Starting point
    x = x0
    y = y0

    # Loop through each step and draw pixels
    for _ in range(int(steps) + 1):
        pygame.draw.circle(screen, RED, (int(round(x)), int(round(y))), 1)
        x += x_inc
        y += y_inc

# Line coordinates
x0, y0 = 100, 200
x1, y1 = 500, 300

# Call the DDA function
draw_dda(x0, y0, x1, y1)

# Update the display
pygame.display.update()

# Wait until user closes the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
