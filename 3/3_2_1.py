from random import randint

a = [randint(0, 1000) for _ in range(randint(10, 20))]
print("Длина массива = ", len(a))
print(a)
for i in range(0, len(a) if len(a) % 2 == 0 else len(a)-1, 2):
     a[i], a[i+1] = a[i+1], a[i]
print(a)
