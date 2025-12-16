def search_element(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"Element found at index {i}")
            return
    print("Element not found")


if __name__ == "__main__":
    search_element([10, 20, 30, 40], 30)
