# Bubble Sort function
def bubblesort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # swap elements
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# test arrays
arr1 = [5, 3, 8, 4, 2]
arr2 = [10, -1, 7, 3, 0]
arr3 = [9, 6, 1, 8, 2]

print("Array 1:", arr1)
print("Sorted:", bubblesort(arr1))
print()

print("Array 2:", arr2)
print("Sorted:", bubblesort(arr2))
print()

print("Array 3:", arr3)
print("Sorted:", bubblesort(arr3))
