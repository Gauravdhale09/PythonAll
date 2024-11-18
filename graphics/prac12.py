import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up figure and axis
fig, ax = plt.subplots()

# Initialize cycle position
x = 0

# Function to draw cycle
def draw_cycle(i):
    global x
    x += 1
    ax.clear()
    ax.set_xlim(0, 800)
    ax.set_ylim(0, 600)
    ax.set_aspect('equal')

    # Draw upper body of cycle
    ax.plot([50 + x, 100 + x], [405, 405], 'w-')
    ax.plot([75 + x, 125 + x], [375, 375], 'w-')
    ax.plot([50 + x, 75 + x], [405, 375], 'w-')
    ax.plot([100 + x, 100 + x], [405, 345], 'w-')
    ax.plot([150 + x, 100 + x], [405, 345], 'w-')
    ax.plot([75 + x, 75 + x], [345, 370], 'w-')
    ax.plot([70 + x, 80 + x], [370, 370], 'w-')
    ax.plot([80 + x, 100 + x], [345, 345], 'w-')

    # Draw wheels
    circle1 = plt.Circle((50 + x, 405), 30, edgecolor='w', facecolor='none')
    circle2 = plt.Circle((150 + x, 405), 30, edgecolor='w', facecolor='none')
    ax.add_artist(circle1)
    ax.add_artist(circle2)

    # Draw road
    ax.plot([0, 800], [436, 436], 'w-')

    # Draw stone
    ax.add_patch(plt.Rectangle((800 - x, 436), 50, 5, edgecolor='w', facecolor='w'))

    if x > 800:
        x = 0

# Create animation
ani = animation.FuncAnimation(fig, draw_cycle, interval=10, repeat=True)

plt.show()