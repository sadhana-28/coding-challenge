def count_odd_even(arr):
    odd = even = 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even count:", even)
    print("Odd count:", odd)


if __name__ == "__main__":
    count_odd_even([1, 2, 3, 4, 5, 6])
