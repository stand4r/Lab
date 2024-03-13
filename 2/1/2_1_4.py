from time import perf_counter
from random import randint
def Cut(n):
    return int(str(n)[1:-1])

start = perf_counter()
for _ in range(1_000_000):
    Cut(randint(1000000, 10000000))
n = randint(1000000, 10000000)
print(n)
print(Cut(n))
end = perf_counter()

print("Время выполнения: ", round(end-start, 2), "с")