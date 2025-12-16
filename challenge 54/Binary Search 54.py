def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            print("Element found at index", mid)
            return
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print("Element not found")


if __name__ == "__main__":
    binary_search([1, 3, 5, 7, 9], 7)
