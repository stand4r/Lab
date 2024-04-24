# Вариант 3

def pos_sum(arr):
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    start_index = min(min_index, max_index)
    end_index = max(min_index, max_index)

    total_sum = 0

    for num in arr[start_index + 1:end_index]:
        if num > 0:
            total_sum += num

    return total_sum

my_array = [3, -5, 2, 8, -1, 6]

print("Сумма положительных чисел между минимальным и максимальным элементами:", pos_sum(my_array))
