import numpy as np

# Parameters
k1 = 1.0           # Attraction coefficient
k2 = 0.1           # Repulsion coefficient
rho = 1.5          # Field tension parameter
R = 1.0            # Radiation strength (for simplicity, uniform for all points)
delta_t = 0.01     # Time step
steps = 100        # Number of simulation steps
interaction_range = 5.0  # Maximum interaction distance

# Initialize positions, velocities, and accelerations for 3 points
points = {
    1: {'position': np.array([0.0, 0.0]), 'velocity': np.array([0.1, 0.2])},
    2: {'position': np.array([1.0, 0.0]), 'velocity': np.array([-0.1, 0.1])},
    3: {'position': np.array([0.0, 1.0]), 'velocity': np.array([0.0, -0.1])},
}

def compute_force(i, j, positions):
    """Compute the force vector exerted on point i by point j."""
    r_ij = positions[j] - positions[i]
    distance = np.linalg.norm(r_ij)
    
    if distance > interaction_range or distance == 0:
        return np.array([0.0, 0.0])  # No interaction beyond range or for self-interaction
    
    force_magnitude = (2 * k1 / distance**3) - (4 * k2 / distance**5)
    return force_magnitude * r_ij

def compute_total_force(i, positions):
    """Compute the total force acting on point i."""
    total_force = np.array([0.0, 0.0])
    for j in positions:
        if i != j:
            total_force += compute_force(i, j, positions)
    return total_force

def compute_radiated_field(acceleration, distance):
    """Compute the radiated field contribution."""
    if distance == 0:
        return np.array([0.0, 0.0])
    return R * acceleration / distance**2

def compute_field_warpage(position, positions, accelerations):
    """Compute the warpage factor at a given position."""
    total_field = np.array([0.0, 0.0])
    for i, pos in positions.items():
        distance = np.linalg.norm(position - pos)
        if distance > 0:
            total_field += compute_radiated_field(accelerations[i], distance)
    return rho * np.linalg.norm(total_field)

# Simulation loop
for step in range(steps):
    positions = {i: data['position'] for i, data in points.items()}
    velocities = {i: data['velocity'] for i, data in points.items()}
    
    # Compute forces and accelerations
    accelerations = {}
    for i in points:
        total_force = compute_total_force(i, positions)
        accelerations[i] = total_force  # Assume unit mass for simplicity
    
    # Update velocities and positions
    for i in points:
        points[i]['velocity'] += accelerations[i] * delta_t
        points[i]['position'] += points[i]['velocity'] * delta_t
    
    # Compute warpage factor for each point
    warpages = {}
    for i in points:
        warpages[i] = compute_field_warpage(points[i]['position'], positions, accelerations)
    
    # Print step results
    print(f"Step {step + 1}:")
    for i, data in points.items():
        print(f"  Point {i}: Position {data['position']}, Warpage {warpages[i]:.4f}")

