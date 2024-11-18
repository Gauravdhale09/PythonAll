import matplotlib.pyplot as plt

def EightWaySymmetricPlot(xc, yc, x, y):
    """ Plot points in all eight symmetric sections of a circle """
    plt.plot(x + xc, y + yc, 'ro')  # Plot in red
    plt.plot(x + xc, -y + yc, 'yo')  # Plot in yellow
    plt.plot(-x + xc, -y + yc, 'go')  # Plot in green
    plt.plot(-x + xc, y + yc, 'yo')  # Plot in yellow
    plt.plot(y + xc, x + yc, 'bo')  # Plot in blue
    plt.plot(y + xc, -x + yc, 'co')  # Plot in cyan
    plt.plot(-y + xc, -x + yc, 'mo')  # Plot in magenta
    plt.plot(-y + xc, x + yc, 'ko')  # Plot in black

def BresenhamCircle(xc, yc, r):
    """ Draw circle using Bresenham's algorithm """
    x = 0
    y = r
    d = 3 - 2 * r
    EightWaySymmetricPlot(xc, yc, x, y)

    while x <= y:
        if d <= 0:
            d = d + (4 * x) + 6
        else:
            d = d + (4 * x) - (4 * y) + 10
            y -= 1
        x += 1
        EightWaySymmetricPlot(xc, yc, x, y)

def main():
    # Ask for user input
    xc = int(input("Enter the value of xc: "))
    yc = int(input("Enter the value of yc: "))
    r = int(input("Enter the value of radius: "))

    # Call BresenhamCircle to draw
    BresenhamCircle(xc, yc, r)

    # Set plot limits
    plt.xlim(xc - r - 10, xc + r + 10)
    plt.ylim(yc - r - 10, yc + r + 10)
    
    # Set aspect of the plot to be equal, so the circle doesn't look like an ellipse
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
