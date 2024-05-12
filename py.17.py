#perform the following operations of tuples 1-create,2-access,3-update,4-delete

# Create tuples
numbers = (1, 2, 3, 4, 5)
fruits = ('apple', 'banana', 'cherry')
empty_tuple = ()

# Access elements in tuples
print("First element of numbers:", numbers[0])
print("Second element of fruits:", fruits[1])

# Attempt to update an element in a tuple (will raise TypeError)
try:
    numbers[0] = 10
except TypeError as e:
    print("TypeError occurred:", e)

# Attempt to delete an element from a tuple (will raise AttributeError)
try:
    del fruits[1]
except AttributeError as e:
    print("AttributeError occurred:", e)
