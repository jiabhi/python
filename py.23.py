#wap to print prime number less than 

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes_less_than(n):
    """Print all prime numbers less than a given number n."""
    print(f"Prime numbers less than {n}:")
    for num in range(2, n):
        if is_prime(num):
            print(num, end=" ")

# Get user input for the upper limit
try:
    limit = int(input("Enter a number to find all prime numbers less than it: "))
    print_primes_less_than(limit)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
