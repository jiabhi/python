#program to handle user define exception

class InvalidInputException(Exception):
    pass

try:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        raise InvalidInputException("Invalid input. Please enter a number.")
    number = int(user_input)
    print(f"You entered the number {number}")
except InvalidInputException as e:
    print(e)