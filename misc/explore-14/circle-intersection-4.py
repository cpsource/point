import math

def circle_relationship(x1, y1, r1, x2, y2, r2):
    """Determine the relationship between two circles: none, inside, tangent, or intersecting."""
    if x1 == x2 and y1 == y2 and r1 == r2:
        return "Identical Circles"

    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if d > r1 + r2:
        return "No Intersection"
    elif d == r1 + r2:
        return "Touching Externally"
    elif abs(r1 - r2) < d < r1 + r2:
        return "Intersecting"
    elif d == abs(r1 - r2):
        return "Touching Internally"
    else:  # d < abs(r1 - r2)
        return "One Inside the Other"

def intersection_properties(x1, y1, r1, x2, y2, r2):
    """Determine the number of intersection points, tangent vectors, and the angle between them."""
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if x1 == x2 and y1 == y2 and r1 == r2:
        return "Infinite", None, None
    
    if d > r1 + r2 or d < abs(r1 - r2):
        return 0, None, None

    # Two intersection points
    if abs(r1 - r2) < d < r1 + r2:
        dx, dy = x2 - x1, y2 - y1
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h = math.sqrt(r1**2 - a**2)

        # Intersection points
        px = x1 + a * (x2 - x1) / d
        py = y1 + a * (y2 - y1) / d
        intersection1 = (px + h * (y2 - y1) / d, py - h * (x2 - x1) / d)
        intersection2 = (px - h * (y2 - y1) / d, py + h * (x2 - x1) / d)

        # Tangent vectors at each intersection point
        tangent1_1 = (-intersection1[1] + y1, intersection1[0] - x1)  # Circle 1
        tangent1_2 = (-intersection2[1] + y1, intersection2[0] - x1)  # Circle 1
        tangent2_1 = (-intersection1[1] + y2, intersection1[0] - x2)  # Circle 2
        tangent2_2 = (-intersection2[1] + y2, intersection2[0] - x2)  # Circle 2

        # Angle between tangents (choose tangents from the same circle)
        dot_product = tangent1_1[0] * tangent1_2[0] + tangent1_1[1] * tangent1_2[1]
        mag_t1 = math.sqrt(tangent1_1[0]**2 + tangent1_1[1]**2)
        mag_t2 = math.sqrt(tangent1_2[0]**2 + tangent1_2[1]**2)
        angle = math.acos(dot_product / (mag_t1 * mag_t2)) if mag_t1 * mag_t2 != 0 else 0

        return 2, [tangent1_1, tangent1_2, tangent2_1, tangent2_2], math.degrees(angle)

    # One intersection point (tangent)
    intersection_x = x1 + (r1 / d) * (x2 - x1)
    intersection_y = y1 + (r1 / d) * (y2 - y1)
    tangent_vector = (-intersection_y + y1, intersection_x - x1)  # Tangent vector
    return 1, tangent_vector, 0

def common_area_and_circumference(x1, y1, r1, x2, y2, r2):
    """Calculate the area and circumference of the intersected region."""
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if x1 == x2 and y1 == y2 and r1 == r2:  # Identical circles
        return math.pi * r1**2, 2 * math.pi * r1

    if d >= r1 + r2:  # No overlap
        return 0, 0
    elif d <= abs(r1 - r2):  # One circle is entirely inside the other
        smaller_radius = min(r1, r2)
        return math.pi * smaller_radius**2, 2 * math.pi * smaller_radius

    # Angles subtended by the intersection points
    theta1 = 2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
    theta2 = 2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))

    # Area of intersection
    area1 = 0.5 * r1**2 * (theta1 - math.sin(theta1))
    area2 = 0.5 * r2**2 * (theta2 - math.sin(theta2))
    common_area = area1 + area2

    # Circumference of the intersected region
    arc_length1 = r1 * theta1
    arc_length2 = r2 * theta2
    common_circumference = arc_length1 + arc_length2

    return common_area, common_circumference

def main():
    x1, y1, r1 = map(float, input("Enter x1, y1, r1 for Circle 1: ").split())
    x2, y2, r2 = map(float, input("Enter x2, y2, r2 for Circle 2: ").split())

    # Determine overall case of interaction
    relationship = circle_relationship(x1, y1, r1, x2, y2, r2)
    print(f"Relationship: {relationship}")

    # Determine intersection points and tangent vectors
    num_points, tangent_vectors, angle = intersection_properties(x1, y1, r1, x2, y2, r2)
    print(f"Number of Intersection Points: {num_points}")
    if tangent_vectors:
        print(f"Tangent Vectors: {tangent_vectors}")
    if angle:
        print(f"Angle Between Tangents: {angle:.2f} degrees")

    # Calculate common area and circumference
    area, circumference = common_area_and_circumference(x1, y1, r1, x2, y2, r2)
    print(f"Common Area: {area:.2f}")
    print(f"Common Circumference: {circumference:.2f}")

if __name__ == "__main__":
    main()

