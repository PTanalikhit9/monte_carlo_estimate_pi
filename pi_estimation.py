
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def monte_carlo_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1

    pi_estimate = 4 * points_inside_circle / num_points
    return pi_estimate

def update(frame, scatter_points, num_points):
    x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
    distance = x**2 + y**2

    if distance <= 1:
        color = 'blue'
    else:
        color = 'red'

    scatter_points.set_offsets(np.vstack((scatter_points.get_offsets(), [x, y])))
    scatter_points.set_array(np.hstack((scatter_points.get_array(), [color])))

    pi_estimate = monte_carlo_pi(frame + 1)
    plt.gca().set_title(f'Monte Carlo Pi Estimation ({frame + 1} points): {pi_estimate:.5f}')

    return scatter_points,

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
scatter_points = ax.scatter([], [], c=[], marker='.', cmap='coolwarm')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(5000), fargs=(scatter_points, 5000), blit=True)

# Show the animation
plt.show()
