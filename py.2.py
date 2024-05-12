#program to find square root in python
import math

def find_square_root(number):
    # Calculate square root using math.sqrt()
    square_root = math.sqrt(number)
    return square_root

# Example usage
number = 25
result = find_square_root(number)
print(f"Square root of {number} is: {result}")