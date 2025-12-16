def print_factorial_pattern(n):
    fact = 1
    num = 1

    for i in range(1, n + 1):
        for _ in range(i):
            fact *= num
            print(fact, end=" ")
            num += 1
        print()
