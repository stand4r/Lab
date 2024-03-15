with open("in.txt", 'r', encoding='utf-8') as file:
    next(file)  # Пропускаем первую строку с количеством учащихся
    students = [line.strip().split() for line in file]

high_achievers = []
for student in students:
    grades = list(map(int, student[2:]))
    if all(grade > 3 for grade in grades):
        high_achievers.append(' '.join(student[:2]))

with open("out.txt", 'w', encoding='utf-8') as file:
    for student in high_achievers:
        file.write(student + '\n')