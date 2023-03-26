
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
