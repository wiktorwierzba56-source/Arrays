# 3x3 zero matrix
matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

# replace main diagonal with 1
for i in range(len(matrix)):
    matrix[i][i] = 1

# print the matrix
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
