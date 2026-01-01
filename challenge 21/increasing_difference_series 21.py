def increasing_difference_series(n):
    value = 1
    diff = 1

    for _ in range(n):
        print(value, end=" ")
        value += diff
        diff += 1


if __name__ == "__main__":
    increasing_difference_series(7)
