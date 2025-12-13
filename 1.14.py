numbers = [5, 2, 9, 1, 5, 6]
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            # compare adjacent elements
            if arr[j] > arr[j + 1]:
                # swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)