#wap to find largest number in python

def find_largest_number_from_input():
    # Prompt user to enter numbers separated by spaces
    input_numbers = input("Enter numbers separated by spaces: ")
    
    # Split input string into a list of numbers
    numbers = [float(num) for num in input_numbers.split()]
    
    # Check if the list is not empty
    if numbers:
        largest_number = max(numbers)
        print(f"The largest number entered is: {largest_number}")
    else:
        print("No numbers entered.")

# Example usage
find_largest_number_from_input()