import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from scipy.spatial import Delaunay

class Bubble:
    def __init__(self, center, radius, view_vector):
        self.center = np.array(center)
        self.radius = radius
        self.view_vector = np.array(view_vector)

    def update(self, dt):
        self.center += np.random.normal(scale=0.1, size=3)
        self.radius += np.random.normal(scale=0.01)
        self.view_vector += np.random.normal(scale=0.01, size=3)
        self.view_vector /= np.linalg.norm(self.view_vector)

def init_bubbles(num_bubbles):
    bubbles = []
    for i in range(num_bubbles):
        center = np.random.normal(scale=10, size=3)
        radius = np.random.uniform(1, 3)
        view_vector = np.random.normal(size=3)
        view_vector /= np.linalg.norm(view_vector)
        bubbles.append(Bubble(center, radius, view_vector))
    return bubbles

def perform_delaunay(bubbles):
    centers = [b.center for b in bubbles]
    tri = Delaunay(centers)
    return tri.simplices

def animate_bubbles(bubbles, simplices):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for simplice in simplices:
        vertices = [bubbles[i].center for i in simplice]
        ax.plot([v[0] for v in vertices], [v[1] for v in vertices], [v[2] for v in vertices], 'k-')

    scat = ax.scatter([b.center[0] for b in bubbles], [b.center[1] for b in bubbles], [b.center[2] for b in bubbles], s=[b.radius**2 for b in bubbles])

    def update(frame):
        for b in bubbles:
            b.update(dt)

        scat._offsets3d = (np.array([b.center[0] for b in bubbles]), np.array([b.center[1] for b in bubbles]), np.array([b.center[2] for b in bubbles]))
        scat._sizes = np.array([b.radius**2 for b in bubbles])

        simplices = perform_delaunay(bubbles)
        for line in ax.lines:
            line.set_linewidth(0)
        for simplice in simplices:
            vertices = [bubbles[i].center for i in simplice]
            ax.plot([v[0] for v in vertices], [v[1] for v in vertices], [v[2] for v in vertices], 'k-')

    ani = FuncAnimation(fig, update, frames=1000, interval=20, blit=False)
    plt.show()

if __name__ == '__main__':
    num_bubbles = 10
    dt = 0.01
    bubbles = init_bubbles(num_bubbles)
    simplices = perform_delaunay(bubbles)
    animate_bubbles(bubbles, simplices)
