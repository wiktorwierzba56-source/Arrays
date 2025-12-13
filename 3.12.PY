arr = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", *arr)
print("Unique elements:", end=" ")

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count == 1:
        print(arr[i], end=" ")
