from random import uniform
def column_characteristic(matrix):
    characteristics = []
    for col in range(len(matrix[0])):
        char = sum(abs(matrix[row][col]) for row in range(len(matrix)) if matrix[row][col] < 0 and matrix[row][col] % 2 != 0)
        characteristics.append(round(char, 2))
    return characteristics

def print_matrix_with_characteristics(matrix, characteristics):
    for i in matrix:
        print(*[f"{round(x, 2):>7}" for x in i])
    print("Characteristics: ", characteristics)
    print()

def swap_columns(matrix, col1, col2):
    for row in matrix:
        row[col1], row[col2] = row[col2], row[col1]


rows = int(input("Количество строк = "))
columns = int(input("Количество столбцов = "))
matrix = [[uniform(-150, 150) for _ in range(columns)] for _ in range(rows)]
print("Исходная матрица:")
characteristics = column_characteristic(matrix)
print_matrix_with_characteristics(matrix, characteristics)
sorted_indices = sorted(range(len(characteristics)), key=lambda k: characteristics[k])
sorted_matrix = [[row[i] for i in sorted_indices] for row in matrix]
sorted_characteristics = [characteristics[i] for i in sorted_indices]
print("Отсортированная матрица:")
print_matrix_with_characteristics(sorted_matrix, sorted_characteristics)