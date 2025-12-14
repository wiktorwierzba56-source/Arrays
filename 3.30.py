def create_multiplication_table():
    table = [[0 for _ in range(5)] for _ in range(5)]
    
    for i in range(5):
        for j in range(5):
            table[i][j] = (i + 1) * (j + 1)
    
    return table
table = create_multiplication_table()

for row in table:
    print(" ".join(map(str, row)))
