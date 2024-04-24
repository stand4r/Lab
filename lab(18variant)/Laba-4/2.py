# Вариант 3

from enum import Enum
import random


class Theme(Enum):
    MATH = "Математика"
    PHYSICS = "Физика"
    CHEMISTRY = "Химия"
    HISTORY = "История"
    LITERATURE = "Литература"


class Question:
    def __init__(self, title, theme):
        self.title = title
        self.theme = theme


class TestSet:
    def __init__(self, questions):
        self.questions = questions


def distribute_questions(questions, num_sets):
    sets = [[] for _ in range(num_sets)]

    for question in questions:
        random_set = random.choice(sets)
        random_set.append(question)

    return [TestSet(test) for test in sets]


num_questions = int(input("Введите количество вопросов: "))
questions = []
for _ in range(num_questions):
    title = input("Введите название вопроса: ")
    theme = input("Введите тематику вопроса (MATH, PHYSICS, CHEMISTRY, HISTORY, LITERATURE): ")
    questions.append(Question(title, Theme[theme]))

num_sets = int(input("Введите количество наборов тестов: "))
test_sets = distribute_questions(questions, num_sets)

for i, test_set in enumerate(test_sets):
    print(f"Набор тестов {i + 1}:")
    for question in test_set.questions:
        print(f"- {question.title} ({question.theme.value})")
