import numpy as np
import matplotlib.pyplot as plt

# Function to compute energy field
# A: amplitude (positive for peaks, negative for wells)
# beta: controls the spread of the Gaussian
# x0, y0: center of the peak or well
def energy_field(x, y, A=1, beta=1, x0=0, y0=0):
    return A * np.exp(-beta * ((x - x0) ** 2 + (y - y0) ** 2))

# Function to create a grid and superimpose multiple energy distortions
def create_energy_field(grid_size, distortions):
    x = np.linspace(-grid_size, grid_size, 500)
    y = np.linspace(-grid_size, grid_size, 500)
    X, Y = np.meshgrid(x, y)

    # Initialize energy field to zero
    field = np.zeros_like(X)

    # Add each distortion (energy peak or well)
    for distortion in distortions:
        A, beta, x0, y0 = distortion
        field += energy_field(X, Y, A, beta, x0, y0)

    return X, Y, field

# Visualization function
def plot_energy_field(X, Y, field):
    plt.figure(figsize=(10, 8))
    plt.contourf(X, Y, field, levels=100, cmap="RdBu_r")
    plt.colorbar(label="Energy Density")
    plt.title("Energy Field Visualization")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

# Main function
def main():
    # Define distortions: (A, beta, x0, y0)
    distortions = [
        (1, 10, -2, -2),  # Energy peak
        (-1, 20, 2, 2),   # Energy well
        (0.5, 15, 0, 3),  # Smaller peak
        (-0.8, 25, -3, -1)  # Smaller well
    ]

    # Create and visualize the energy field
    grid_size = 5
    X, Y, field = create_energy_field(grid_size, distortions)
    plot_energy_field(X, Y, field)

if __name__ == "__main__":
    main()

