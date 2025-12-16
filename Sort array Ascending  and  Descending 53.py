def sort_array(arr, order):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if (order == 'asc' and arr[j] > arr[j + 1]) or \
               (order == 'desc' and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Sorted array:", arr)


if __name__ == "__main__":
    sort_array([4, 2, 7, 1], 'asc')
