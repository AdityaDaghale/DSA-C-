"""Array Operations - Linear & Binary Search"""

def linear_search(arr, target):
    """Linear search - O(n)"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """Binary search - O(log n)"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    print("Linear Search for 7:", linear_search(arr, 7))
    print("Binary Search for 7:", binary_search(arr, 7))
