def identity_matrix(n):
    matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

matrix_3 = identity_matrix(3)
matrix_5 = identity_matrix(5)
matrix_8 = identity_matrix(8)

print("Macierz jednostkowa o rozmiarze 3:")
print_matrix(matrix_3)

print("Macierz jednostkowa o rozmiarze 5:")
print_matrix(matrix_5)

print("Macierz jednostkowa o rozmiarze 8:")
print_matrix(matrix_8)
