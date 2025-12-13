t = (50, 20, 40, 50, 30, 50)

value = int(input("Value: "))

count = 0
for item in t:
    if item == value:
        count += 1

print("Tuple:", *t)
print("Value:", value)
print("Number of occurrences:", count)
