import math

def hybrid_transfer_function(velocity, position, alpha=1, gamma=1):
    """
    Computes the hybrid transfer function T(v, x) based on the sigmoid (velocity) and Lorentzian (position) components.

    Parameters:
        velocity (float): The velocity of the particle (v).
        position (float): The position or spatial interaction parameter (x).
        alpha (float): Scaling factor for the sigmoid function (default: 1).
        gamma (float): Width parameter for the Lorentzian function (default: 1).

    Returns:
        float: The computed value of the hybrid transfer function T(v, x).
    """
    # Sigmoid function for velocity component
    sigmoid_velocity = 1 / (1 + math.exp(-alpha * velocity))

    # Lorentzian function for position component
    lorentzian_position = 1 / (1 + (position**2) / (gamma**2))

    # Hybrid transfer function combines sigmoid and Lorentzian components
    hybrid_value = sigmoid_velocity * lorentzian_position

    return hybrid_value

def main():
    """
    Main function to demonstrate the hybrid transfer function with various test cases.
    """
    # Test cases with different velocities and positions
    test_cases = [
        {"velocity": 0, "position": 0, "alpha": 1, "gamma": 1},  # Both zero
        {"velocity": 1, "position": 0.5, "alpha": 1, "gamma": 1},  # Moderate values
        {"velocity": -1, "position": 2, "alpha": 2, "gamma": 1},  # Negative velocity
        {"velocity": 3, "position": 5, "alpha": 0.5, "gamma": 2},  # Large values
        {"velocity": 0.5, "position": -3, "alpha": 1, "gamma": 0.1},  # Small gamma
    ]

    # Iterate over test cases and compute hybrid transfer function
    print("Hybrid Transfer Function Results")
    print("----------------------------------")
    for i, case in enumerate(test_cases, 1):
        velocity = case["velocity"]
        position = case["position"]
        alpha = case["alpha"]
        gamma = case["gamma"]

        # Compute hybrid transfer function
        result = hybrid_transfer_function(velocity, position, alpha, gamma)

        # Print results with detailed information
        print(f"Test Case {i}:")
        print(f"  Velocity (v): {velocity}")
        print(f"  Position (x): {position}")
        print(f"  Alpha (sigmoid scaling): {alpha}")
        print(f"  Gamma (Lorentzian width): {gamma}")
        print(f"  Hybrid Transfer Function T(v, x): {result:.5f}")
        print("----------------------------------")

if __name__ == "__main__":
    main()

