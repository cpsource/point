import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Process

# Parameters (same as before)
k1 = 1.0
k2 = 0.1
rho = 1.5
R = 1.0
delta_t = 0.01
steps = 100
interaction_range = 5.0

# Initialize positions and velocities
points = {
    1: {'position': np.array([0.0, 0.0]), 'velocity': np.array([0.1, 0.2])},
    2: {'position': np.array([1.0, 0.0]), 'velocity': np.array([-0.1, 0.1])},
    3: {'position': np.array([0.0, 1.0]), 'velocity': np.array([0.0, -0.1])},
}

# Simulation functions
def compute_force(i, j, positions):
    r_ij = positions[j] - positions[i]
    distance = np.linalg.norm(r_ij)
    if distance > interaction_range or distance == 0:
        return np.array([0.0, 0.0])
    force_magnitude = (2 * k1 / distance**3) - (4 * k2 / distance**5)
    return force_magnitude * r_ij

def compute_total_force(i, positions):
    total_force = np.array([0.0, 0.0])
    for j in positions:
        if i != j:
            total_force += compute_force(i, j, positions)
    return total_force

# Trajectory Simulation
def simulate_trajectories():
    trajectories = {i: [points[i]['position'].copy()] for i in points}
    for step in range(steps):
        positions = {i: points[i]['position'] for i in points}
        velocities = {i: points[i]['velocity'] for i in points}
        accelerations = {i: compute_total_force(i, positions) for i in points}
        for i in points:
            points[i]['velocity'] += accelerations[i] * delta_t
            points[i]['position'] += points[i]['velocity'] * delta_t
            trajectories[i].append(points[i]['position'].copy())
    return trajectories

def plot_trajectories():
    trajectories = simulate_trajectories()
    plt.figure(figsize=(8, 8))
    for i, trajectory in trajectories.items():
        trajectory = np.array(trajectory)
        plt.plot(trajectory[:, 0], trajectory[:, 1], label=f"Point {i}")
        plt.scatter(trajectory[0, 0], trajectory[0, 1], marker='o', label=f"Start {i}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Trajectories of Points")
    plt.legend()
    plt.grid(True)
    plt.show()

# Run in a separate process
if __name__ == "__main__":
    p1 = Process(target=plot_trajectories)
    p1.start()

