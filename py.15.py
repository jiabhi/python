#wap to demonstrate use of user defined module , built in modeule

# Import user-defined module
import my_module

# Import built-in module
import math

def main():
    # Calculate area of a circle using user-defined module
    radius = 5
    area = my_module.calculate_circle_area(radius)
    print(f"Area of a circle with radius {radius} units is: {area:.2f} square units")

    # Calculate square root using built-in module
    number = 25
    square_root = math.sqrt(number)
    print(f"Square root of {number} is: {square_root:.2f}")

# Execute the main function
if _name_ == "_main_":
    main()
