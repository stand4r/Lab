# Вариант 3
import random

def rand_str(length):
    characters = ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '5', '6', '7', '8', '9', '?', '!', ';']
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def repl(string):
    return string.replace('?', '_')

l = int(input("Введите длину строки: "))
random_string = rand_str(l)
print("Строка с случайными символами:", random_string)
processed_string = repl(random_string)
print("Строка после замены символов:", processed_string)
