array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Tablica przed zmianami:")
for row in array:
    print(row)

for row in array:
    row[0], row[-1] = row[-1], row[0]

print("\nTablica po zmianach:")
for row in array:
    print(row)
