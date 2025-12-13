names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

print("Names:", end=" ")
for name in names:
    print(name, end=" ")

print()

longest = names[0]

for name in names:
    if len(name) > len(longest):
        longest = name

print("Longest name:", longest)
