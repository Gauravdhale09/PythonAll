import matplotlib.pyplot as plt
import time
import math
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Function to draw clock hands
def draw_hand(length, angle, color):
    x_center = screen_width // 2
    y_center = screen_height // 2
    x = x_center + length * math.cos(math.radians(angle))
    y = y_center - length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, (x_center, y_center), (x, y), 2)

# Function to draw clock face
def draw_clock_face():
    x_center = screen_width // 2
    y_center = screen_height // 2
    radius = 200
    pygame.draw.circle(screen, WHITE, (x_center, y_center), radius, 2)
    for i in range(12):
        angle = i * 30
        x_inner = x_center + (radius - 20) * math.cos(math.radians(angle))
        y_inner = y_center - (radius - 20) * math.sin(math.radians(angle))
        x_outer = x_center + radius * math.cos(math.radians(angle))
        y_outer = y_center - radius * math.sin(math.radians(angle))
        pygame.draw.line(screen, WHITE, (x_inner, y_inner), (x_outer, y_outer), 1)

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current time
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the clock face
    draw_clock_face()

    # Draw hour, minute, and second hands
    draw_hand(100, (hours * 30 + minutes / 2), BLUE)  # Hour hand
    draw_hand(150, (minutes * 6), GREEN)  # Minute hand
    draw_hand(170, (seconds * 6), RED)  # Second hand

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)