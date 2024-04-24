import math

def calc_expr(a, b, d, t):
    numerator = (3 * math.sin(b ** t * math.exp(d ** 3)) - 4 * math.sin(b ** t * math.exp(d ** 3)) ** 2)
    denominator = (math.cos(a ** t * math.log(d ** 2)) ** 2 - math.cos(a ** t * math.exp(d ** 3)) ** 2)
    result = numerator / denominator
    return result

a = int(input("Введите значение a:"))
b = int(input("Введите значение b:"))
d = int(input("Введите значение d:"))
t = int(input("Введите значение t:"))
result = calc_expr(a, b, d, t)
print("Результат вычисления:", result)
