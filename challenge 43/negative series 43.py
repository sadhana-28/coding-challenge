def generate_series(n):
    value = 1
    sign = 1

    for _ in range(n):
        print(sign * value, end=" ")
        value += 4
        sign *= -1


if __name__ == "__main__":
    generate_series(6)
