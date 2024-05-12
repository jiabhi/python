#wap to print current date and time

import datetime

def print_current_date_and_time():
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Print the current date and time in a formatted way
    print("Current Date and Time:", current_datetime)

# Call the function to print current date and time
print_current_date_and_time()