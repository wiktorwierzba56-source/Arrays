def separate_even_odd(arr):
    even_numbers = [x for x in arr if x % 2 == 0]  # Liczby parzyste
    odd_numbers = [x for x in arr if x % 2 != 0]   # Liczby nieparzyste
    return even_numbers + odd_numbers  # Łączymy listy parzystych i nieparzystych

arr = [7, 9, 2, 4, 5, 6]
result = separate_even_odd(arr)
print("Odd and Even numbers:", result)
