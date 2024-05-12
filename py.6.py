#wap to find out the prime number in python

def is_prime(n):
    # Check if n is less than 2 (prime numbers must be greater than 1)
    if n <= 1:
        return False
    
    # Check for divisibility from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor other than 1 and itself
    
    return True  # No divisors other than 1 and itself, hence prime

# Example usage
num = 17

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")