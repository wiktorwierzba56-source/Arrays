arr = [15, 8, 31, 47, 2, 19]

print("Array:", end=" ")
for value in arr:
    print(value, end=" ")

print()

total = 0
for value in arr:
    total += value

mean = total / len(arr)

print("Arithmetic mean:", mean)