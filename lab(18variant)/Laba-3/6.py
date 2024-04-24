# Вариант 3
def substr(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    
    return any(string2[i:i+len1] == string1 for i in range(len2 - len1 + 1))


string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

if substr(string1, string2):
    print("Первая строка является подстрокой второй строки.")
else:
    print("Первая строка не является подстрокой второй строки.")
