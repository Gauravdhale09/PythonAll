import matplotlib.pyplot as plt

def drawline(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    x, y = x0, y0
    p = 2 * dy - dx
    x_points = [x]
    y_points = [y]

    while x < x1:
        if p >= 0:
            y += 1
            p = p + 2 * dy - 2 * dx
        else:
            p = p + 2 * dy
        x += 1
        x_points.append(x)
        y_points.append(y)
    
    return x_points, y_points

def main():
    # Taking input from the user
    x0, y0 = map(int, input("Enter coordinates of first point (x0, y0): ").split())
    x1, y1 = map(int, input("Enter coordinates of second point (x1, y1): ").split())

    # Getting the line coordinates using Bresenham's algorithm
    x_points, y_points = drawline(x0, y0, x1, y1)

    # Plotting the points
    plt.plot(x_points, y_points, marker='o', color='black')
    plt.title("Bresenham's Line Drawing Algorithm")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.gca().invert_yaxis()  # To match the pixel-like coordinate system
    plt.show()

if __name__ == '__main__':
    main()
