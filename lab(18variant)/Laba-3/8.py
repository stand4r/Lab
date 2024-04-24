# Вариант 3
import random

def random_mx(rows, columns):
    mx = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(columns)]
        mx.append(row)
    return mx

mx1 = random_mx(2, 2)
mx2 = random_mx(3, 2)
mx3 = random_mx(2, 3)

def find_column_min(mx):
    min_columns = []
    for j in range(len(mx[0])):
        min_column = min(row[j] for row in mx)
        min_columns.append(min_column)
    return min_columns

val_mx1 = find_column_min(mx1)
val_mx2 = find_column_min(mx2)
val_mx3 = find_column_min(mx3)

print("Минимумы в каждом столбце матрицы 1:", val_mx1)
print("Минимумы в каждом столбце матрицы 2:", val_mx2)
print("Минимумы в каждом столбце матрицы 3:", val_mx3)

total_min_sum = sum(val_mx1) + sum(val_mx2) + sum(val_mx3)
print("Сумма всех минимумов:", total_min_sum)
