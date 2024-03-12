from random import randint

M = int(input("M = "))
N = int(input("N = "))
matrix = [[randint(0, 200) for _ in range(M)] for _ in range(N)]
for i in matrix:
    print(*[f"{x:>3}" for x in i])
print("Максимальные значения по столбцам: ", end="")
for i in range(M):
    max = 0
    for x in range(N):
        if matrix[x][i] > max:
            max = matrix[x][i]
    print(max, end=" ")
print()
even = 0
count = 0
for i in matrix:
    for x in i:
        if x % 2 == 1:
            even += x
            count+= 1
print("Среднее значение нечетных элементов =", round(even/count, 2))