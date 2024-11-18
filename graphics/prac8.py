import matplotlib.pyplot as plt
import numpy as np
import random
import time
from matplotlib.patches import Arc  # Import Arc from patches

# Screen dimensions
ScreenWidth = 800
ScreenHeight = 600
GroundY = int(ScreenHeight * 0.75)

# Global variable for left displacement
ldisp = 0

# Function to create a hut
def draw_hut():
    plt.fill_between([150, 250], 180, 300, color='brown')  # Hut base
    plt.fill_between([250, 420], 180, 300, color='brown')  # Hut base extension
    plt.fill_between([180, 220], 250, 300, color='brown')  # Door

    # Roof lines
    plt.plot([200, 150], [100, 180], color='white')  # Left roof
    plt.plot([200, 250], [100, 180], color='white')  # Right roof
    plt.plot([200, 370], [100, 100], color='white')  # Top roof
    plt.plot([370, 420], [100, 180], color='white')  # Right roof

# Function to draw a man with an umbrella
def draw_man_and_umbrella(x, ldisp):
    # Head
    head = plt.Circle((x, GroundY - 90), 10, color='black')
    plt.gca().add_artist(head)

    # Body
    plt.plot([x, x], [GroundY - 80, GroundY - 30], color='black')
    plt.plot([x, x + 10], [GroundY - 70, GroundY - 60], color='black')
    plt.plot([x, x + 10], [GroundY - 65, GroundY - 55], color='black')
    plt.plot([x + 10, x + 20], [GroundY - 60, GroundY - 70], color='black')
    plt.plot([x + 10, x + 20], [GroundY - 55, GroundY - 70], color='black')

    # Umbrella
    plt.plot([x, x + ldisp], [GroundY - 30, GroundY], color='black')
    plt.plot([x, x - ldisp], [GroundY - 30, GroundY], color='black')

    # Umbrella top using Arc
    umbrella_top = Arc((x + 20, GroundY - 120), 40, 40, angle=0, theta1=0, theta2=180, color='black')
    plt.gca().add_artist(umbrella_top)
    plt.plot([x + 20, x + 20], [GroundY - 120, GroundY - 70], color='black')

# Function to create rainfall
def rain(x):
    for _ in range(400):
        rx = random.randint(0, ScreenWidth)
        ry = random.randint(0, ScreenHeight)
        if ry < GroundY - 4:
            if ry < GroundY - 120 or (ry > GroundY - 120 and (rx < x - 20 or rx > x + 60)):
                plt.plot([rx, rx + 0.5], [ry, ry + 4], color='blue')

# Function to create a rainbow
def draw_rainbow():
    global ldisp
    ldisp = (ldisp + 2) % 20
    draw_man_and_umbrella(x, ldisp)
    draw_hut()
    
    for i in range(30, 100):
        plt.plot(np.linspace(ScreenWidth / 5, ScreenWidth * 4 / 5, 100), 
                 np.linspace(ScreenHeight / 5, ScreenHeight / 5, 100), 
                 color=str(i / 100))
        time.sleep(0.05)
        plt.pause(0.05)

# Driver code
plt.figure(figsize=(8, 6))
plt.xlim(0, ScreenWidth)
plt.ylim(0, ScreenHeight)
plt.axis('off')  # Hide axes

x = 0
while True:
    draw_hut()
    plt.plot(ScreenWidth - 100, 50, 'yo', markersize=20)  # Sun
    plt.fill_between([ScreenWidth - 100, ScreenWidth - 100], 0, 50, color='yellow')  # Sun fill
    plt.axhline(y=GroundY, color='black', linewidth=2)  # Ground
    rain(x)
    
    ldisp = (ldisp + 2) % 20
    draw_man_and_umbrella(x, ldisp)
    plt.pause(0.02)
    plt.clf()  # Clear figure for next frame
    x = (x + 2) % ScreenWidth

    if plt.waitforbuttonpress(0):  # Exit loop if any key is pressed
        break

draw_rainbow()
plt.show()
