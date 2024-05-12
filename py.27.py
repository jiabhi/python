#wap to demontrate math built in function

import math

# Input values
x = 10
y = -5.5
angle_degrees = 45

# Demonstrate math built-in functions
print(f"Input values: x = {x}, y = {y}, angle (in degrees) = {angle_degrees}\n")

# Demonstrate math functions
print(f"Absolute value of y: {math.fabs(y)}")
print(f"Square root of x: {math.sqrt(x)}")
print(f"Sine of {angle_degrees} degrees: {math.sin(math.radians(angle_degrees)):.4f}")
print(f"Cosine of {angle_degrees} degrees: {math.cos(math.radians(angle_degrees)):.4f}")
print(f"Tangent of {angle_degrees} degrees: {math.tan(math.radians(angle_degrees)):.4f}")
print(f"Ceiling of y: {math.ceil(y)}")
print(f"Floor of y: {math.floor(y)}")
