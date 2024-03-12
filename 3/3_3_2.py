from random import randint

N = int(input("Количество элементв: "))
arr = [randint(1, 9) for _ in range(N)]
print(*arr)
for i in range(1, 10):
    print(arr.count(i), end=" ")
print()