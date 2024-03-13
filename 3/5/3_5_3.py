from random import uniform
def local_minima(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    local_mins = []

    for i in range(rows):
        for j in range(cols):
            current = matrix[i][j]
            if ((i == 0 or current < matrix[i-1][j]) and
                    (i == rows-1 or current < matrix[i+1][j]) and
                    (j == 0 or current < matrix[i][j-1]) and
                    (j == cols-1 or current < matrix[i][j+1])):
                local_mins.append((i, j, current))
    return local_mins

rows = int(input("Количество строк = "))
columns = int(input("Количество столбцов = "))
matrix = [[uniform(-150, 150) for _ in range(columns)] for _ in range(rows)]
print("\nИсходная матрица")
for i in matrix:
    print(*[f"{round(x, 2):>7}" for x in i])
print("\nЛокальные минимумы")
print(*local_minima(matrix))