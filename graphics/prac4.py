import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define PI constant
PI = 3.14159265

# Define 3D point structure
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Initial cube vertices
cube = [
    Point3D(-50, -50, -50),
    Point3D(50, -50, -50),
    Point3D(50, 50, -50),
    Point3D(-50, 50, -50),
    Point3D(-50, -50, 50),
    Point3D(50, -50, 50),
    Point3D(50, 50, 50),
    Point3D(-50, 50, 50)
]

# Function to create cube faces for rendering
def get_cube_faces():
    return [
        [cube[0], cube[1], cube[2], cube[3]],
        [cube[4], cube[5], cube[6], cube[7]],
        [cube[0], cube[1], cube[5], cube[4]],
        [cube[2], cube[3], cube[7], cube[6]],
        [cube[0], cube[3], cube[7], cube[4]],
        [cube[1], cube[2], cube[6], cube[5]]
    ]

# Function to translate the cube
def translate(tx, ty, tz):
    for p in cube:
        p.x += tx
        p.y += ty
        p.z += tz

# Function to rotate the cube around the X-axis
def rotateX(angle):
    rad = angle * (PI / 180)
    for p in cube:
        y = p.y * np.cos(rad) - p.z * np.sin(rad)
        z = p.y * np.sin(rad) + p.z * np.cos(rad)
        p.y = y
        p.z = z

# Function to rotate the cube around the Y-axis
def rotateY(angle):
    rad = angle * (PI / 180)
    for p in cube:
        x = p.x * np.cos(rad) + p.z * np.sin(rad)
        z = -p.x * np.sin(rad) + p.z * np.cos(rad)
        p.x = x
        p.z = z

# Function to rotate the cube around the Z-axis
def rotateZ(angle):
    rad = angle * (PI / 180)
    for p in cube:
        x = p.x * np.cos(rad) - p.y * np.sin(rad)
        y = p.x * np.sin(rad) + p.y * np.cos(rad)
        p.x = x
        p.y = y

# Function to scale the cube
def scale(sx, sy, sz):
    for p in cube:
        p.x *= sx
        p.y *= sy
        p.z *= sz

# Function to plot the cube
def plot_cube():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Get cube faces for rendering
    faces = get_cube_faces()
    
    # Plot each face of the cube
    for face in faces:
        ax.add_collection3d(Poly3DCollection([[(p.x, p.y, p.z) for p in face]], color='cyan', edgecolors='r', linewidths=1, alpha=0.25))
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    ax.set_xlim([-200, 200])
    ax.set_ylim([-200, 200])
    ax.set_zlim([-200, 200])
    
    plt.show()

# Main loop for user input and transformations
def main():
    while True:
        plot_cube()  # Display the cube

        # Display transformation options
        print("\nChoose a transformation:")
        print("1. Translation")
        print("2. Rotation (X-axis)")
        print("3. Rotation (Y-axis)")
        print("4. Rotation (Z-axis)")
        print("5. Scaling")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            tx = float(input("Enter translation vector (tx): "))
            ty = float(input("Enter translation vector (ty): "))
            tz = float(input("Enter translation vector (tz): "))
            translate(tx, ty, tz)
        elif choice == 2:
            angle = float(input("Enter rotation angle (in degrees) around X-axis: "))
            rotateX(angle)
        elif choice == 3:
            angle = float(input("Enter rotation angle (in degrees) around Y-axis: "))
            rotateY(angle)
        elif choice == 4:
            angle = float(input("Enter rotation angle (in degrees) around Z-axis: "))
            rotateZ(angle)
        elif choice == 5:
            sx = float(input("Enter scaling factor (sx): "))
            sy = float(input("Enter scaling factor (sy): "))
            sz = float(input("Enter scaling factor (sz): "))
            scale(sx, sy, sz)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
