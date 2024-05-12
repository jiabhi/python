#define a module to find fibonacci number & import module to another program

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return "Invalid input. n should be a positive integer."

    # Base cases
    if n == 1:
        return 0  # 1st Fibonacci number
    elif n == 2:
        return 1  # 2nd Fibonacci number

    # Compute Fibonacci sequence for n > 2
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b

    return b  # nth Fibonacci number