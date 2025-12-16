def find_max(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    print("Maximum:", maximum)


if __name__ == "__main__":
    find_max([4, 2, 9, 1, 7])
