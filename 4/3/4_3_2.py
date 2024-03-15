with open("in.txt", 'r', encoding='utf-8') as file:
    next(file)  # Пропускаем первую строку с количеством учащихся
    students = [line.strip().split() for line in file]


math_avg = sum(int(student[2]) for student in students) / len(students)
phys_avg = sum(int(student[3]) for student in students) / len(students)
it_avg = sum(int(student[4]) for student in students) / len(students)

averages = [(sum(map(int, student[2:])) / 3, ' '.join(student[:2])) for student in students]
max_avg = max(averages, key=lambda x: x[0])[0]

best_students = [student[1] for student in averages if student[0] == max_avg]

with open("out.txt", 'w', encoding='utf-8') as file:
    file.write(f'{math_avg} {phys_avg} {it_avg}\n')
    for student in best_students:
        file.write(student + '\n')
