def find_min(arr):
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    print("Minimum:", minimum)


if __name__ == "__main__":
    find_min([4, 2, 9, 1, 7])
