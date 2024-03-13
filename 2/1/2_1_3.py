def Reverse(n):
    return int(str(n)[::-1])

from random import randint
from time import time
time_start = time()
for _ in range(1_000_000):
    Reverse(randint(0, 100000))
time_end = time()
n = randint(0, 100000)
print("Example:")
print("  N:", n)
print("  Reverse N:", Reverse(n))
print("\nTime:", round(time_end-time_start, 2), "s")