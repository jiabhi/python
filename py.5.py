 #wap to find a value using binary search in python

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Found the target, return its index
        elif arr[mid] < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Target not found

# Example usage
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

# Perform binary search
result_index = binary_search(sorted_list, target_value)

if result_index != -1:
    print(f"Target value {target_value} found at index: {result_index}")
else:
    print(f"Target value {target_value} not found in the list")
