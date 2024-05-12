#wap to demostrate working with tuples


# Define a tuple of fruits
fruits = ('apple', 'banana', 'cherry', 'date')

# Access elements of the tuple
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Iterate through the tuple
for fruit in fruits:
    print(fruit)

# Tuple unpacking
first, second, third, fourth = fruits
print("First fruit:", first)
print("Second fruit:", second)
print("Third fruit:", third)
print("Fourth fruit:", fourth)

# Concatenate tuples
more_fruits = ('grape', 'kiwi', 'mango')
all_fruits = fruits + more_fruits
print("All fruits:", all_fruits)

# Slicing a tuple
print("First two fruits:", all_fruits[:2])
print("Last three fruits:", all_fruits[-3:])

# Check membership in a tuple
print("'banana' in all fruits:", 'banana' in all_fruits)
print("'pear' in all fruits:", 'pear' in all_fruits)

# Create a single element tuple
single_element_tuple = ('apple',)

# Attempting to modify a tuple (will raise TypeError)
try:
    fruits[0] = 'orange'
except TypeError as e:
    print("TypeError occurred:", e)
