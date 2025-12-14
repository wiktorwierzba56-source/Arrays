def count_greater_than(arr, value):
    return len([x for x in arr if x > value])

numbers = [7, 3, 8, 5, 2]
value = float(input("Podaj wartość do porównania: "))
print(f"Liczba elementów większych niż {value}: {count_greater_than(numbers, value)}")
