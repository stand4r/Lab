# Вариант 4
def sort_nums(arr):
    zeros_index = 0
    twos_index = len(arr) - 1

    i = 0
    while i <= twos_index:
        if arr[i] == 0:
            arr[i], arr[zeros_index] = arr[zeros_index], arr[i]
            zeros_index += 1
            i += 1
        elif arr[i] == 2:
            arr[i], arr[twos_index] = arr[twos_index], arr[i]
            twos_index -= 1
        else:
            i += 1

arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

sort_nums(arr)

print("Переставленный массив:", arr)
