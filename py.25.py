#wap to convert temperature to fahrenhit

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Get user input for temperature in Celsius
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
except ValueError:
    print("Invalid input. Please enter a valid temperature in Celsius (e.g., 25.5)")