def print_fibonacci_pattern(n):
    a, b = 1, 1

    for i in range(1, n + 1):
        for _ in range(i):
            print(a, end=" ")
            a, b = b, a + b
        print()
