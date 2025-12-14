def is_subset(arr1, arr2):
    return all(x in arr2 for x in arr1)  # Sprawdzamy, czy wszystkie elementy arr1 znajdują się w arr2

arr1 = [2, 4, 6]
arr2 = [2, 4, 6, 7, 9, 5]
result = is_subset(arr1, arr2)
print("Is arr1 a subset of arr2?", result)
