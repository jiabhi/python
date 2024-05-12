#wap to perform various arithmetic operator an number in pyhton

a = 10
b = 3

# Perform arithmetic operations
sum_result = a + b
difference_result = a - b
product_result = a * b
division_result = a / b
integer_division_result = a // b  # Integer division (floor division)
remainder_result = a % b  # Modulus (remainder)
power_result = a ** b  # Exponentiation (a raised to the power of b)

# Display the results
print("Arithmetic Operations with Numbers:")
print(f"{a} + {b} = {sum_result}")
print(f"{a} - {b} = {difference_result}")
print(f"{a} * {b} = {product_result}")
print(f"{a} / {b} = {division_result:.2f}")  # Display division result with 2 decimal places
print(f"{a} // {b} = {integer_division_result}")
print(f"{a} % {b} = {remainder_result}")
print(f"{a} ** {b} = {power_result}")
