def search_2d(matrix, key):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == key:
                print("Element found at position", i, j)
                return
    print("Element not found")


if __name__ == "__main__":
    search_2d([[1, 2], [3, 4]], 3)
