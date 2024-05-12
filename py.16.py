#perform the following operations of dicttionaries 1-create,2-access,3-update,4-delete

# Create a dictionary of student information
student = {
    'name': 'John Doe',
    'age': 20,
    'grade': 'A',
    'courses': ['Math', 'Science', 'English']
}

print("Initial Student Dictionary:", student)

# Access values in the dictionary
print("\nStudent Name:", student['name'])
print("Student Age:", student['age'])
print("Student Courses:", student['courses'])

# Update values in the dictionary
student['age'] = 21
student['grade'] = 'B'
student['courses'].append('History')

print("\nUpdated Student Dictionary:", student)

# Delete items from the dictionary
del student['grade']  # Delete 'grade' key and its value
removed_courses = student.pop('courses')  # Remove 'courses' key and return its value

print("\nRemoved Courses:", removed_courses)
print("Updated Student Dictionary after Deletion:", student)
