# Вариант 3

import random

def count_negative_num(arr):
    return sum(1 for num in arr if num < 0)

def sum_num(arr):
    return sum(num for num in arr if num % 2 == 0)

def max_pos_num(arr):
    return max((num, i) for i, num in enumerate(arr) if num > 0)[1]

def print_elem_chet(arr):
    for i in range(0, len(arr), 2):
        print(f'a[{i}] = {arr[i]}')

array = [random.randint(-150, 150) for _ in range(15)]

print("Количество отрицательных чисел:", count_negative_num(array))
print("Сумма четных чисел:", sum_num(array))
print("Индекс максимального положительного числа:", max_pos_num(array))
print("Элементы с четными индексами:")
print_elem_chet(array)
