# Вариант 3

import random

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def min_in_col(matrix):
    mins = []
    for col in range(len(matrix[0])):
        column_values = [row[col] for row in matrix]
        min_value = min(column_values)
        mins.append(min_value)
    return mins

def negative_elem_avr(matrix):
    negative_elements = []
    for row in matrix:
        for element in row:
            if element < 0:
                negative_elements.append(element)
    if negative_elements:
        return sum(negative_elements) / len(negative_elements)
    else:
        return 0


N = int(input("Введите количество столбцов матрицы:")) 
M = int(input("Введите количество строк матрицы:")) 

my_matrix = [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]

print("Матрица:")
print_matrix(my_matrix)

min_in_columns = min_in_col(my_matrix)
print("\nМинимальные элементы в каждом столбце:")
print(" ".join(map(str, min_in_columns)))

average_negative = negative_elem_avr(my_matrix)
print("\nСреднее значение для всех отрицательных элементов матрицы:", average_negative)
