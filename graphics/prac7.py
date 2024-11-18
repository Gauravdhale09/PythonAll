import matplotlib.pyplot as plt
import numpy as np
import time

# Function to move the drawing cursor
def move(j, h, x, y):
    if j == 1:
        y -= h
    elif j == 2:
        x += h
    elif j == 3:
        y += h
    elif j == 4:
        x -= h
    return x, y

# Hilbert curve drawing function
def hilbert(r, d, l, u, i, h, x, y, points):
    if i > 0:
        i -= 1
        hilbert(d, r, u, l, i, h, x, y, points)
        x, y = move(r, h, x, y)
        points.append((x, y))
        time.sleep(0.1)  # Delay to visualize the drawing process
        hilbert(r, d, l, u, i, h, x, y, points)
        x, y = move(d, h, x, y)
        points.append((x, y))
        time.sleep(0.1)
        hilbert(r, d, l, u, i, h, x, y, points)
        x, y = move(l, h, x, y)
        points.append((x, y))
        time.sleep(0.1)
        hilbert(u, l, d, r, i, h, x, y, points)

def main():
    n = int(input("Give the value of n: "))
    x0, y0 = 50, 150
    h = 10
    r, d, l, u = 2, 3, 4, 1

    points = [(x0, y0)]
    x, y = x0, y0

    hilbert(r, d, l, u, n, h, x, y, points)

    # Unzip points for plotting
    x_points, y_points = zip(*points)

    # Create a plot
    plt.plot(x_points, y_points, marker='o', color='black')
    plt.title("Hilbert Curve of Order {}".format(n))
    plt.axis('equal')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
