def fibonacci_series(n):
    a, b = 1, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    fibonacci_series(8)
