def fill_matrix_spirally(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top = 0
    left = 0
    bottom = n - 1
    right = n - 1
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    return matrix

n = int(input("Введите размер матрицы N:"))  

spiral_matrix = fill_matrix_spirally(n)

for i in spiral_matrix:
    print(*[f"{round(x, 2):>5}" for x in i])
