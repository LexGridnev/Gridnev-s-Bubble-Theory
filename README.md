# Bubble Theory of Gridnev (BTG) - Python Implementation
This is a Python implementation of the Bubble Theory of Gridnev (BTG), a theoretical framework that describes subjective reality as a set of interconnected bubbles. Each bubble represents a person's perception of reality, and the intersections between bubbles represent shared experiences.


### The main characteristics of a bubble in the BTG are:

* Center coordinates
* Radius
* Vector that describes the direction of view within the bubble
 
### This implementation includes the following functions:

* init_bubbles: initializes a set of bubbles with random coordinates, radii, and view vectors.
* update_bubbles: updates the coordinates of the bubbles based on their view vectors and a given time step dt.
* find_neighbors: finds the neighboring bubbles of a given bubble based on their intersections.
* draw_bubbles: visualizes the bubbles and their intersections using Matplotlib.
* animate_bubbles: animates the bubbles and their intersections using Matplotlib.
In addition, the implementation includes a method for adding the "jitter" effect, which simulates a trembling motion of the bubbles.

The BTG is based on the Delaunay triangulation, which ensures that the bubbles are connected without overlapping. The implementation allows for changing the view vector of a bubble to slide towards another bubble, with several possible methods to calculate this vector.

# Usage

To use this implementation of the BTG, 
#### simply run the main.py script.
By default, the script initializes 10 bubbles and animates their movements for a total of 10 seconds. The resulting animation is saved in the output folder as a .gif file.

You can customize the number of bubbles and the duration of the animation by changing the num_bubbles and duration variables in the script. You can also customize the appearance of the bubbles and the animation by modifying the relevant Matplotlib parameters in the draw_bubbles and animate_bubbles functions.

# Requirements

This implementation requires Python 3.x and the following Python packages:

* NumPy
* Matplotlib
You can install these packages using pip:

pip install numpy matplotlib


Acknowledgments

The Bubble Theory of Gridnev was proposed by Russian philosopher and mathematician Alexey Gridnev. This implementation is based on the ideas presented in his work.

## References
- Gridnev, A. (2003). Bubble Theory of Consciousness. Vanaheimr: Respublika.
- Delaunay triangulation: https://en.wikipedia.org/wiki/Delaunay_triangulation

![Bubble portal](https://github.com/LexGridnev/Gridnev-s-Bubble-Theory/blob/main/345edbbbc7684b86880d80404dab5f00.jpeg)
