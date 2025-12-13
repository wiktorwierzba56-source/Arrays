arr = [34, 7, 19, 4, 21, 8]

count_even = 0
i = 0

while i < len(arr):
    if arr[i] % 2 == 0:   # check if even
        count_even += 1
    i += 1

print("Number of even values:", count_even)
