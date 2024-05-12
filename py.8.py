#wap to calculate area of triangle using heron's formula in python

import math

def calculate_area_using_herons_formula(a, b, c):
    # Calculate semi-perimeter
    s = (a + b + c) / 2

    # Calculate area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area

# Example usage
side1 = 3
side2 = 4
side3 = 5

# Calculate area of the triangle
area_of_triangle = calculate_area_using_herons_formula(side1, side2, side3)

print(f"The area of the triangle with sides {side1}, {side2}, {side3} is: {area_of_triangle:.2f} square units")
