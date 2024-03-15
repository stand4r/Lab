from enum import Enum, auto

class Specialty(Enum):
    RПИС = auto()  # Разработка программно-информационных систем
    ПО = auto()    # Программная инженерия
    УИТС = auto()  # Управление и информационные технологии в системах

class Student:
    def __init__(self, name, spec):
        self.name = name
        self.spec = spec

    def __repr__(self):
        return f"{self.name} ({self.spec.name})"


def distribute_students(students, num_groups):
    groups = [[] for _ in range(num_groups)]
    groups_counter = {spec: [0]*num_groups for spec in Specialty}

    for student in students:
        # Найдем группу с минимальным количеством студентов той же специальности
        min_group = groups_counter[student.spec].index(min(groups_counter[student.spec]))
        # Добавляем студента в эту группу
        groups[min_group].append(student)
        # Увеличиваем счетчик студентов специальности в этой группе
        groups_counter[student.spec][min_group] += 1

    return groups


students = [
    Student("Иванов", Specialty.RПИС),
    Student("Петров", Specialty.ПО),
    Student("Сидоров", Specialty.УИТС),
    Student("Смирнов", Specialty.RПИС),
    Student("Кузнецов", Specialty.ПО)
]

# Распределяем студентов по 2 группам
groups = distribute_students(students, 2)

# Выводим результаты распределения
for i, group in enumerate(groups, start=1):
    print(f"Группа {i}: {', '.join(map(str, group))}")
