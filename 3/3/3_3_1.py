def merge_sorted_arrays(arr1, arr2):
    merged_array = [None] * (len(arr1) + len(arr2))

    i = j = k = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array[k] = arr1[i]
            i += 1
        else:
            merged_array[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        merged_array[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        merged_array[k] = arr2[j]
        j += 1
        k += 1
    
    return merged_array

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

merged_arr = merge_sorted_arrays(arr1, arr2)
print(merged_arr)
