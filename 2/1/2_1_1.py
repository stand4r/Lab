from time import perf_counter
from random import randint
def MaxDigit(n):
    m = 0
    for i in str(n):
        if int(i) == 9:
            return 9
        if int(i) > int(m):
            m = i
    return m

start = perf_counter()
for _ in range(1_000_000):
    MaxDigit(randint(1000000, 10000000))
n = randint(1000000, 10000000)
print(n)
print(MaxDigit(n))
end = perf_counter()

print("Время выполнения: ", round(end-start, 2), "с")