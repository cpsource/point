```
import math
from scipy.integrate import quad

def hybrid_transfer_function(v, x, alpha=1, gamma=1):
    """
    Computes the hybrid transfer function T(v, x) based on the sigmoid (velocity) and Lorentzian (position) components.

    Parameters:
        v (float): The velocity of the particle (v).
        x (float): The position or spatial interaction parameter (x).
        alpha (float): Scaling factor for the sigmoid function (default: 1).
        gamma (float): Width parameter for the Lorentzian function (default: 1).

    Returns:
        float: The computed value of the hybrid transfer function T(v, x).
    """
    # Sigmoid function for velocity component
    sigmoid_velocity = 1 / (1 + math.exp(-alpha * v))

    # Lorentzian function for position component
    lorentzian_position = 1 / (1 + (x**2) / (gamma**2))

    # Hybrid transfer function combines sigmoid and Lorentzian components
    hybrid_value = sigmoid_velocity * lorentzian_position

    return hybrid_value

def line_integral(alpha=1, gamma=1, k=1, t1=0, t2=1):
    """
    Computes the line integral of the hybrid transfer function along a straight-line path.

    Parameters:
        alpha (float): Scaling factor for the sigmoid function.
        gamma (float): Width parameter for the Lorentzian function.
        k (float): Slope of the straight-line path.
        t1 (float): Starting parameter value.
        t2 (float): Ending parameter value.

    Returns:
        float: The computed line integral value.
    """
    def integrand(t):
        v = t  # Velocity as a function of t
        x = k * t  # Position as a function of t
        ds = math.sqrt(k**2 + 1)  # Arc length element for the straight line
        return hybrid_transfer_function(v, x, alpha, gamma) * ds

    # Numerically integrate the hybrid transfer function along the path
    result, _ = quad(integrand, t1, t2)
    return result

def main():
    """
    Main function to demonstrate the line integral computation with various test cases.
    """
    # Parameters for the hybrid transfer function and path
    alpha = 1
    gamma = 1
    k = 1  # Slope of the path
    t1 = 0  # Start of the parameter range
    t2 = 2  # End of the parameter range

    # Compute the line integral
    result = line_integral(alpha, gamma, k, t1, t2)

    # Print the result
    print("Line Integral of the Hybrid Transfer Function:")
    print(f"  Parameters: alpha={alpha}, gamma={gamma}, k={k}, t1={t1}, t2={t2}")
    print(f"  Result: {result:.5f}")

if __name__ == "__main__":
    main()

```

