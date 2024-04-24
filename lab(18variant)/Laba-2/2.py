# Вариант 3
def sumFunction(n):
    if n < 10:
        return 0
    elif 10 <= n <= 99:
        return n + sumFunction(n - 1)
    else:
        return sumFunction(n - 1)


result = sumFunction(99)
print("Сумма всех двузначных чисел:", result)
