def sum_of_positive_numbers(arr):
    if not arr or len(arr) == 1:
        return 0
    
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))
    
    if min_index > max_index:
        min_index, max_index = max_index, min_index
    
    sum_positive = sum(x for x in arr[min_index+1:max_index] if x > 0)
    
    return sum_positive

arr = [3, -1, 4, 0, 5, -2, 2, 7]
print(arr)
print(sum_of_positive_numbers(arr)) 