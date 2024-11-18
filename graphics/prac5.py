import matplotlib.pyplot as plt
import numpy as np

# Function to plot and fill the polygon using Scanline algorithm
def scanline_polygon_fill(n, a):
    # Store the polygon edges
    x_coords, y_coords = zip(*a)
    x_coords += (x_coords[0],)  # Close the polygon
    y_coords += (y_coords[0],)
    
    # Draw the polygon outline
    plt.plot(x_coords, y_coords, 'k-')  # Draw the polygon with black lines

    # Initialize intersection array and slopes
    slopes = []
    xi = [0] * n

    # Calculate inverse slopes
    for i in range(n):
        dy = a[i + 1][1] - a[i][1]
        dx = a[i + 1][0] - a[i][0]
        if dy == 0:
            slopes.append(1.0)
        elif dx == 0:
            slopes.append(0.0)
        else:
            slopes.append(dx / dy)

    # Scanline fill between y min and y max
    y_min = min(y_coords)
    y_max = max(y_coords)

    for y in range(y_min, y_max):
        k = 0
        for i in range(n):
            if ((a[i][1] <= y and a[i + 1][1] > y) or (a[i][1] > y and a[i + 1][1] <= y)):
                xi[k] = int(a[i][0] + slopes[i] * (y - a[i][1]))
                k += 1

        # Sort the x-intersections
        xi = sorted(xi[:k])

        # Fill between pairs of intersections
        for i in range(0, k - 1, 2):
            plt.plot([xi[i], xi[i + 1]], [y, y], 'r-')  # Filling line with red color

    plt.show()

# Input the number of edges and coordinates of the polygon
n = int(input("Enter the number of edges of the polygon: "))

a = []
for i in range(n):
    x, y = map(int, input(f"Enter X{i} Y{i}: ").split())
    a.append((x, y))
a.append(a[0])  # Close the polygon by adding the first point at the end

# Call the scanline fill function
scanline_polygon_fill(n, a)
