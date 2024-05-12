#wap if the number is even or odd in python

def check_even_or_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

# Example usage
number = 25
result = check_even_or_odd(number)
print(result)