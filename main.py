'''
This Python code defines a Bubble class and initializes a number of random bubbles, represented as instances of the Bubble class.
The script performs Delaunay triangulation on the centers of the bubbles, and animates the bubbles while showing the triangulation. 
The animation simulates the movement of the bubbles by updating their center, radius, and view_vector attributes in a random fashion over time. 
The triangulation is redrawn at each update frame, and the bubbles are redrawn based on their updated attributes. 
The final output is an animation of the moving bubbles with the Delaunay triangulation overlaid.
'''



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.spatial import Delaunay

# Define the Bubble class
class Bubble:
    def __init__(self, center, radius, view_vector):
        self.center = np.array(center)
        self.radius = radius
        self.view_vector = np.array(view_vector)

    def update(self, dt):
        # Simulate the bubble's movement
        self.center += np.random.normal(scale=0.1, size=3)
        self.radius += np.random.normal(scale=0.01)
        self.view_vector += np.random.normal(scale=0.01, size=3)
        self.view_vector /= np.linalg.norm(self.view_vector)

# Initialize bubbles
def init_bubbles(num_bubbles):
    bubbles = []
    for i in range(num_bubbles):
        center = np.random.normal(scale=10, size=3)
        radius = np.random.uniform(1, 3)
        view_vector = np.random.normal(size=3)
        view_vector /= np.linalg.norm(view_vector)
        bubbles.append(Bubble(center, radius, view_vector))
    return bubbles

# Perform Delaunay triangulation on the bubble centers
def perform_delaunay(bubbles):
    centers = [b.center for b in bubbles]
    tri = Delaunay(centers)
    return tri.simplices

# Animate the bubbles
def animate_bubbles(bubbles, simplices):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)

    # Draw the Delaunay triangles
    for simplice in simplices:
        vertices = [bubbles[i].center[:2] for i in simplice]
        ax.plot([v[0] for v in vertices], [v[1] for v in vertices], 'k-')

    # Draw the bubbles
    scat = ax.scatter([b.center[0] for b in bubbles], [b.center[1] for b in bubbles], s=[b.radius**2 for b in bubbles])

    def update(frame):
        # Update the bubbles
        for b in bubbles:
            b.update(dt)

        # Redraw the bubbles
        scat.set_offsets(np.array([[b.center[0], b.center[1]] for b in bubbles]))
        scat.set_sizes(np.array([b.radius**2 for b in bubbles]))

        # Redraw the Delaunay triangles
        simplices = perform_delaunay(bubbles)
        for line in ax.lines:
            line.set_linewidth(0)
        for simplice in simplices:
            vertices = [bubbles[i].center[:2] for i in simplice]
            ax.plot([v[0] for v in vertices], [v[1] for v in vertices], 'k-')

    ani = FuncAnimation(fig, update, frames=1000, interval=20, blit=False)
    plt.show()

if __name__ == '__main__':
    num_bubbles = 10
    dt = 0.01
    bubbles = init_bubbles(num_bubbles)
    simplices = perform_delaunay(bubbles)
    animate_bubbles(bubbles, simplices)
