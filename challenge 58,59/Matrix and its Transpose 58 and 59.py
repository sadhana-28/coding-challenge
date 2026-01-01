matrix = [[1, 2, 3], [4, 5, 6]]
rows = len(matrix)
cols = len(matrix[0])

transpose = [[0]*rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

print("Matrix:")
for row in matrix:
    print(row)

print("Transpose:")
for row in transpose:
    print(row)
