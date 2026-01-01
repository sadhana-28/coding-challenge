def print_square_alternate_pattern(n):
    num = 1
    sign = 1

    for i in range(1, n + 1):
        for _ in range(i):
            value = (num * num) * sign
            print(value, end=" ")
            sign *= -1
            num += 1
        print()
