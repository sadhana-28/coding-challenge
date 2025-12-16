def series_23(n):
    if n <= 0:
        return

    series = [1]
    differences = [3, 3, 5, 11]  # observed pattern

    for i in range(1, n):
        diff = differences[i - 1] if i - 1 < len(differences) else differences[-1]
        series.append(series[-1] + diff)

    for num in series:
        print(num, end=" ")


if __name__ == "__main__":
    series_23(5)
