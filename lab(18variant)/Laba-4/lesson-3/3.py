#Вариант 3
def input_students():
    students = []
    while True:
        surname = input("Введите фамилию студента (или введите 'готово' для завершения ввода): ")
        if surname.lower() == 'готово':
            break
        name = input("Введите имя студента: ")
        try:
            average_score = float(input("Введите средний балл студента: "))
        except ValueError:
            print("Средний балл должен быть числом. Попробуйте снова.")
            continue
        students.append({"фамилия": surname, "имя": name, "средний балл": average_score})
    return students

students = input_students()

sorted_students = sorted(students, key=lambda x: x["средний балл"], reverse=True)

with open("out.txt", "w") as file:
    for student in sorted_students:
        file.write(f"{student['фамилия']} {student['имя']} ({student['средний балл']})\n")

