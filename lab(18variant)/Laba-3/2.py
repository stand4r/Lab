# Вариант 1

def swap_elements(arr):
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]


my_array = [1, 2, 3, 4, 5, 6]

swap_elements(my_array)

print("Массив после обмена соседними ячейками:", my_array)
