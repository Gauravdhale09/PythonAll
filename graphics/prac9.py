import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots()

# Set the aspect ratio to be equal
ax.set_aspect('equal')

# Define the rectangle
rect = patches.Rectangle((250, 100), 400, 180, 
                         edgecolor='black', facecolor='green')

# Add the rectangle to the axes
ax.add_patch(rect)

# Set the limits of the axes
ax.set_xlim(0, 800)
ax.set_ylim(0, 500)

# Hide the axes
plt.axis('off')

# Show the plot
plt.show()