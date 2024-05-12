#wap to demonstrate string built in funtction

s = input("Enter a string: ")

print(f"Length: {len(s)}")
print(f"Uppercase: {s.upper()}")
print(f"Lowercase: {s.lower()}")
print(f"Capitalized: {s.capitalize()}")

substring = input("Enter a substring to count: ")
print(f"Count of '{substring}': {s.count(substring)}")

substring_to_find = input("Enter a substring to find: ")
index = s.find(substring_to_find)
print(f"Index of '{substring_to_find}': {index if index != -1 else 'Not found'}")

old_substring, new_substring = input("Enter a substring to replace and its replacement (separated by space): ").split()
print(f"String after replacement: '{s.replace(old_substring, new_substring)}'")