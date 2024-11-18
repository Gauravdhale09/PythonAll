import matplotlib.pyplot as plt
import numpy as np

def draw_triangle(x1, y1, x2, y2, x3, y3):
    """ Function to draw a triangle using matplotlib """
    plt.plot([x1, x2], [y1, y2], 'r-')  # Line from (x1, y1) to (x2, y2)
    plt.plot([x2, x3], [y2, y3], 'r-')  # Line from (x2, y2) to (x3, y3)
    plt.plot([x3, x1], [y3, y1], 'r-')  # Line from (x3, y3) to (x1, y1)

def translate(x, y, tx, ty):
    """ Translate the points by tx and ty """
    return x + tx, y + ty

def rotate(x, y, angle):
    """ Rotate the points around the origin by angle degrees """
    rad = np.radians(angle)
    newX = x * np.cos(rad) - y * np.sin(rad)
    newY = x * np.sin(rad) + y * np.cos(rad)
    return newX, newY

def scale(x, y, sx, sy):
    """ Scale the points by factors sx and sy """
    return x * sx, y * sy

def main():
    # Input the coordinates of the triangle
    x1, y1 = map(int, input("Enter the coordinates of point 1 (x1, y1): ").split())
    x2, y2 = map(int, input("Enter the coordinates of point 2 (x2, y2): ").split())
    x3, y3 = map(int, input("Enter the coordinates of point 3 (x3, y3): ").split())

    while True:
        # Clear the plot for every iteration
        plt.clf()

        # Draw the original triangle
        plt.title("2D Triangle Transformation")
        draw_triangle(x1, y1, x2, y2, x3, y3)

        # Set plot limits and aspect ratio
        plt.xlim(-100, 200)
        plt.ylim(-100, 200)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid(True)

        plt.draw()  # Render the plot
        plt.pause(1)  # Pause for 1 second to view

        # Display options
        print("\nChoose a transformation:")
        print("1. Translation")
        print("2. Rotation")
        print("3. Scaling")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:  # Translation
            tx, ty = map(int, input("Enter translation vector (tx, ty): ").split())
            x1, y1 = translate(x1, y1, tx, ty)
            x2, y2 = translate(x2, y2, tx, ty)
            x3, y3 = translate(x3, y3, tx, ty)

        elif choice == 2:  # Rotation
            angle = float(input("Enter rotation angle (in degrees): "))
            x1, y1 = rotate(x1, y1, angle)
            x2, y2 = rotate(x2, y2, angle)
            x3, y3 = rotate(x3, y3, angle)

        elif choice == 3:  # Scaling
            sx, sy = map(float, input("Enter scaling factors (sx, sy): ").split())
            x1, y1 = scale(x1, y1, sx, sy)
            x2, y2 = scale(x2, y2, sx, sy)
            x3, y3 = scale(x3, y3, sx, sy)

        elif choice == 4:  # Exit
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

    plt.show()  # Final display of the plot

if __name__ == "__main__":
    main()
