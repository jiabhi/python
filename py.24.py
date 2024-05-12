#wap to find factorial of number using recurssion in python

def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input for the number
try:
    num = int(input("Enter a non-negative integer to calculate its factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")