# Вариант 3

import random

def rand_mx(rows, cols):
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

def count_min(matrix):
    local_minima = []

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            neighbors = [matrix[i+x][j+y] for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)]
            if matrix[i][j] < min(neighbors):
                local_minima.append((i, j))

    return local_minima

def visualize_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


N = int(input("Введите количество столбцов матрицы:")) 
M = int(input("Введите количество строк матрицы:")) 

random_matrix = rand_mx(M, N)

print("Исходная матрица:")
visualize_matrix(random_matrix)

local_minima = count_min(random_matrix)
print("\nЛокальные минимумы:")
for minimum in local_minima:
    print(f"({minimum[0]}, {minimum[1]})")
