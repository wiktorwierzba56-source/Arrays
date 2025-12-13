arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

print("Numbers in the first array not in the second array:")

for value in arr1:
    found = False
    for v in arr2:
        if value == v:
            found = True
            break
    if not found:
        print(value, end=" ")
