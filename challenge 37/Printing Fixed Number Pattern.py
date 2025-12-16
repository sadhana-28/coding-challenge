def print_fixed_number_pattern(n):
    row = "".join(str(i) for i in range(1, n + 1))
    for _ in range(n):
        print(row)
