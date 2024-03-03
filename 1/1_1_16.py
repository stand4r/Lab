from random import randint

print("Исходное выражение: 226 у.е.")
from math import *
a = randint(1, 100)
b = randint(1, 100)
t = randint(2, 10)
print(f"a={a}")
print(f"b={b}")
print(f"t={t}")

az = log1p(a*t**2)
bz = log10(b)
y = sin(az+bz)/(cos(az)*cos(bz))
print("y=", round(y, 2))
print("Преобразованное: 101 y.e.")