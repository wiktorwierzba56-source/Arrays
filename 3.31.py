array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_value = array[0][0]
max_value = array[0][0]
min_position = (0, 0)
max_position = (0, 0)

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] < min_value:
            min_value = array[i][j]
            min_position = (i, j)
        if array[i][j] > max_value:
            max_value = array[i][j]
            max_position = (i, j)

print(f"Najmniejsza wartość to {min_value}, znajduje się w wierszu {min_position[0]}, kolumnie {min_position[1]}")
print(f"Największa wartość to {max_value}, znajduje się w wierszu {max_position[0]}, kolumnie {max_position[1]}")
