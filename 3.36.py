def flatten_2d_to_1d(matrix):
    return [item for row in matrix for item in row]

array_1 = [
    [2, 3],
    [1, 5]
]
array_2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]
array_3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

def print_1d_array(array):
    print(" ".join(map(str, array)))

print("Tablica 1D dla array_1:")
print_1d_array(flatten_2d_to_1d(array_1))

print("Tablica 1D dla array_2:")
print_1d_array(flatten_2d_to_1d(array_2))

print("Tablica 1D dla array_3:")
print_1d_array(flatten_2d_to_1d(array_3))
