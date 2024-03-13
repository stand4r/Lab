from random import randint

M = int(input("M = "))
N = int(input("N = "))
matrix = [[randint(-200, 200) for _ in range(M)] for _ in range(N)]
for i in matrix:
    print(*[f"{x:>3}" for x in i])
print("Минимальные значения по столбцам: ", end="")
for i in range(M):
    min = 201
    for x in range(N):
        if matrix[x][i] < min:
            max = matrix[x][i]
    print(max, end=" ")
print()
even = 0
count = 0
for i in matrix:
    for x in i:
        if x < 0:
            even += x
            count+= 1
print("Среднее значение отрицательных элементов =", round(even/count, 2))