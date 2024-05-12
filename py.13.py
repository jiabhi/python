 #wap to demonstrate working with dictionaries

student = {
    'name': 'John Doe',
    'age': 20,
    'grade': 'A',
    'courses': ['Math', 'Science', 'English']
}

# Accessing values using keys
print("Student Name:", student['name'])
print("Student Age:", student['age'])
print("Student Grade:", student['grade'])
print("Student Courses:", ', '.join(student['courses']))

# Iterating through the dictionary
print("\nIterating through the dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# Checking if a key exists in the dictionary
print("\nChecking if 'grade' is in student:")
if 'grade' in student:
    print("Grade:", student['grade'])

# Adding a new key-value pair
student['city'] = 'New York'
print("\nStudent City:", student['city'])

# Updating a value for an existing key
student['age'] = 21
print("Updated Student Age:", student['age'])

# Removing a key-value pair
removed_courses = student.pop('courses', [])
print("\nRemoved Courses:", ', '.join(removed_courses))
print("Updated Student Info:", student)
