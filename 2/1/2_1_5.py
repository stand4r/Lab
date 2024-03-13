from time import perf_counter
from random import randint
def UpToTen(n):
    m = ""
    for i in str(n):
        if i == 0:
            m += "0"
        else:
            m += str(10-int(i))
    return int(m)

start = perf_counter()
for _ in range(1_000_000):
    UpToTen(randint(1000000, 10000000))
n = randint(1000000, 10000000)
print(n)
print(UpToTen(n))
end = perf_counter()

print("Время выполнения: ", round(end-start, 2), "с")