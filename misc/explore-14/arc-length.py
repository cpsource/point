import math

# xc, yc center of circle
# x1, y1 first point on circle
# x2, y2 second point on circle

def arc_length(x1, y1, x2, y2, xc, yc, r):
    # Vectors from the center to the points
    v1 = (x1 - xc, y1 - yc)
    v2 = (x2 - xc, y2 - yc)
    
    # Dot product and magnitudes
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude = r  # For points on the circle, magnitude equals radius
    
    # Central angle (in radians)
    theta = math.acos(dot_product / (magnitude * magnitude))
    
    # Determine the direction of the angle
    cross_product = (v1[0] * v2[1]) - (v1[1] * v2[0])
    if cross_product < 0:  # Clockwise direction
        theta = 2 * math.pi - theta
    
    # Arc length
    arc_length = r * theta
    return arc_length

# Example usage
x1, y1 = 1, 0
x2, y2 = 0, 1
xc, yc = 0, 0
r = 1
length = arc_length(x1, y1, x2, y2, xc, yc, r)
print(f"Arc Length: {length:.5f}")

