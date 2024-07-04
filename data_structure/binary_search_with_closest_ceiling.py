def binary_search_recursive(arr, target, low, high, closest_ceiling):
    if low > high:
        return closest_ceiling

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, closest_ceiling)
    else:
        # Update closest_ceiling if arr[mid] is a better candidate
        closest_ceiling = mid
        return binary_search_recursive(arr, target, low, mid - 1, closest_ceiling)


# Wrapper function to simplify the initial call
def binary_search(arr, target):
    result = binary_search_recursive(arr, target, 0, len(arr) - 1, -1)
    if result != -1:
        return result
    else:
        print("Ceiling element not found in the array")
        return -1


# Example usage
if __name__ == "__main__":
    arr = [1, 5, 8, 15]
    target = 788
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}, which is {arr[result]}")
    else:
        print("Element not found and no ceiling element present in the array")
