Below are two programs: one for **visualizing trajectories** and another for **visualizing field distortions**. They run in separate windows simultaneously by leveraging Python's `matplotlib` and `multiprocessing` modules. 

---

### **Program 1: Visualizing Trajectories**

This program plots the paths of the points over time.

```python
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
```

---

### **Program 2: Visualizing Field Distortions**

This program visualizes the field distortions as a heatmap.

```python
import matplotlib.pyplot as plt
import numpy as np

# Function to compute field warpage
def compute_radiated_field(acceleration, distance):
    if distance == 0:
        return np.array([0.0, 0.0])
    return R * acceleration / distance**2

def compute_field_warpage_grid(points, accelerations, grid_size=50, field_range=2.0):
    x = np.linspace(-field_range, field_range, grid_size)
    y = np.linspace(-field_range, field_range, grid_size)
    X, Y = np.meshgrid(x, y)
    field_magnitude = np.zeros_like(X)

    for i, accel in accelerations.items():
        for gx in range(grid_size):
            for gy in range(grid_size):
                position = np.array([X[gx, gy], Y[gx, gy]])
                r = np.linalg.norm(position - points[i]['position'])
                if r > 0:
                    field_magnitude[gx, gy] += np.linalg.norm(compute_radiated_field(accel, r))

    return X, Y, field_magnitude

def simulate_field_distortion():
    positions = {i: points[i]['position'] for i in points}
    accelerations = {i: compute_total_force(i, positions) for i in points}
    X, Y, field = compute_field_warpage_grid(points, accelerations)
    plt.figure(figsize=(8, 8))
    plt.contourf(X, Y, field, levels=50, cmap="viridis")
    plt.colorbar(label="Field Distortion")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Field Distortion Heatmap")
    plt.grid(True)
    plt.show()

# Run in a separate process
if __name__ == "__main__":
    p2 = Process(target=simulate_field_distortion)
    p2.start()
```

---

### **How to Run Both Programs Simultaneously**

1. Copy **Program 1** and **Program 2** into two separate Python scripts (e.g., `trajectories.py` and `field_distortion.py`).
2. Run both scripts in parallel:
   ```bash
   python3 trajectories.py &
   python3 field_distortion.py &
   ```
   This launches two separate windows for the trajectories and the field distortions.

---

### **Enhancements**
- Add real-time updates for the field heatmap by integrating the simulation loop directly with `matplotlib.animation`.
- Combine both visualizations into a single script with separate subplots.

Would you like help combining the two into a single interactive program or further optimizing the visualizations? 😊

