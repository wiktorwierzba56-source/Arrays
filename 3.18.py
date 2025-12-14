def second_largest(arr):
    arr_sorted = sorted(arr, reverse=True)
    return arr_sorted[1]  # Drugi największy element

def largest_smallest_difference(arr):
    largest = max(arr)
    smallest = min(arr)
    return largest - smallest  # Różnica

def median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 1:
        return arr_sorted[n // 2]  # Jeśli liczba elementów jest nieparzysta, zwróć środkowy element
    else:
        return (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) / 2  # Jeśli liczba elementów jest parzysta, zwróć średnią dwóch środkowych

def smallest_largest(arr):
    smallest = min(arr)
    largest = max(arr)
    return [smallest, largest]  # Zwróć najmniejszy i największy element jako listę

def array_to_string(arr):
    return '-'.join(map(str, arr))  # Zwróć elementy jako ciąg znaków oddzielony myślnikami

numbers = [7, 3, 8, 5, 2]

print("Numbers:", array_to_string(numbers))
print("Second largest number:", second_largest(numbers))
print("Median:", median(numbers))
print("Smallest and largest number:", smallest_largest(numbers))
print("Numbers as a string:", array_to_string(numbers))
