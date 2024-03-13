from random import uniform
def find_saddle_point(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        row_min = min(matrix[i])
        min_col_index = matrix[i].index(row_min)
        
        col_max = max(row[min_col_index] for row in matrix)
        
        if row_min == col_max:
            print(f"Седловая точка находится в строке {i+1}, столбце {min_col_index+1}")
            return (i+1, min_col_index+1)
    
    print("Седловой точки нет")
    return 0
rows = int(input("Количество строк = "))
columns = int(input("Количество столбцов = "))
matrix = [[uniform(-150, 150) for _ in range(columns)] for _ in range(rows)]
find_saddle_point(matrix)
