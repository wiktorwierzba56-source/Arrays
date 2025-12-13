arr = [15, 8, 31, 47, 2, 19]

# print array
i = 0
print("Array:", end=" ")
while i < len(arr):
    print(arr[i], end=" ")
    i += 1

print()

total = 0
i = 0
while i < len(arr):
    total += arr[i]
    i += 1

mean = total / len(arr)

print("Arithmetic mean:", mean)
