from random import randint
def find_min_in_rows(matrix):
    return [min(row) for row in matrix]

def average_without_extremes(matrix):
    flat_matrix = [item for row in matrix for item in row]
    flat_matrix.sort()
    return sum(flat_matrix[1:-1]) / (len(flat_matrix) - 2)


M = int(input("M = "))
N = int(input("N = "))
matrix = [[randint(-100, 200) for _ in range(M)] for _ in range(N)]
for i in matrix:
    print(*[f"{x:>3}" for x in i])
print("Минимальные значения по строкам: ", end="")
print(find_min_in_rows(matrix))
print()

print("Среднее значение элементов, без max и min =", round(average_without_extremes(matrix),2))