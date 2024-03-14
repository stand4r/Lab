from random import randint
arr = [[[randint(-100, 100) for _ in range(2)] for _ in range(2)], [[randint(-100, 100) for _ in range(3)] for _ in range(2)], [[randint(-100, 100) for _ in range(2)] for _ in range(3)]]
print("Исходные матрицы")
for matrix in arr:
    for i in matrix:
        print(*[f"{round(x, 2):>4}" for x in i])
    print("")
S = 0
print("\nМинимумы в столбцах")
for matrix in arr:
    m = 101
    for i in range(len(matrix[0])):
        for n in range(len(matrix)):
            if m > matrix[n][i]:
                m = matrix[n][i]
        print(m)
        S+=m
        m = 101
print(f"Сумма: {S}")