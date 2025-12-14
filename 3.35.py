def transpose_matrix(m):
    return [list(row) for row in zip(*m)]
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]
matrix_3 = [
    [5, 6, 7],
    [8]
]
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

print("Transponowana macierz 1:")
transposed_matrix_1 = transpose_matrix(matrix_1)
print_matrix(transposed_matrix_1)

print("Transponowana macierz 2:")
transposed_matrix_2 = transpose_matrix(matrix_2)
print_matrix(transposed_matrix_2)

print("Transponowana macierz 3:")
transposed_matrix_3 = transpose_matrix(matrix_3)
print_matrix(transposed_matrix_3)
