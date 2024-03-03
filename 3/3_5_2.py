from random import uniform 

rows = int(input("Количество строк = "))
columns = int(input("Количество столбцов = "))
matrix = [[uniform(-150, 150) for _ in range(columns)] for _ in range(rows)]
print("\nИсходная матрица")
new_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
for i in matrix:
    print(*[f"{round(x, 2):>7}" for x in i])
for i in range(rows):
    for j in range(columns):
        total = 0
        count = 0
        for k in range(max(0, i-1), min(rows, i+2)):
            for l in range(max(0, j-1), min(columns, j+2)):
                if (i, j) != (k, l):
                    total+=matrix[k][l]
                    count+=1
        new_matrix[i][j] = total/count
print("\nСглаженная матрица")
for i in new_matrix:
    print(*[f"{round(x, 2):>7}" for x in i])
