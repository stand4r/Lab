s = input("Введите фразу: ")
c = 1
for i in s:
    if i == " ":
        c+=1
c+=1
print(f"Количество слов: {c}\n")
