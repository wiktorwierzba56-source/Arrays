import random

def rand_elem(arr):
    return random.choice(arr)

arr = [7, 3, 8, 5, 2]
for _ in range(5):
    print(rand_elem(arr))
