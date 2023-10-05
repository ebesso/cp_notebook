#Array should already be sorted
def bin_search(array, target):
    right = len(array) - 1
    left = 0

    while left <= right:
        mid = (right + left) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1

    return -1
