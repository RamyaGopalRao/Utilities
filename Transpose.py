import random

rows = 6
cols = 8
actual=[[0 for _ in range(rows)] for _ in range(cols)]
print(actual)
matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

for i in range(rows-1):
    for j in range(cols-1):
        actual[j][i]=matrix[i][j]
print(matrix)
print(actual)
