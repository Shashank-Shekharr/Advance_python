def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [2, 4, 6, 8, 10]
key = 6
result = binary_search(arr, key)
print(f'Element found at index {result}' if result != -1 else 'Element not found')