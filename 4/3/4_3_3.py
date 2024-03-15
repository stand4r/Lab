
with open("in.txt", 'r', encoding='utf-8') as file:
    next(file)  # Пропускаем первую строку с количеством учащихся
    students = [line.strip().split() for line in file]
averages = sorted([(sum(map(int, student[2:])) / 3, ' '.join(student[:2])) for student in students], key=lambda x: x[0], reverse=True)

with open("out.txt", 'w', encoding='utf-8') as file:
    for avg, student in averages:
        file.write(f'{student} {avg}\n')
