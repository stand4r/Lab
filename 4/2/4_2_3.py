from enum import Enum
from collections import defaultdict

# Определение перечисления для тем вопросов
class Theme(Enum):
    MATH = 1
    SCIENCE = 2
    HISTORY = 3
    LITERATURE = 4

# Класс, представляющий вопрос
class Question:
    def __init__(self, name, theme):
        self.name = name
        self.theme = theme

def distribute_questions(questions, n_sets):
    # Словарь для сбора наборов тестов
    test_sets = defaultdict(list)
    
    # Счетчики для каждой темы, чтобы следить за распределением
    theme_counts = {theme: 0 for theme in Theme}
    
    for question in questions:
        # Находим набор с минимальным количеством вопросов этой темы
        min_theme_count = min(theme_counts.values())
        target_set = None
        for i in range(n_sets):
            if theme_counts[question.theme] == min_theme_count and len(test_sets[i]) < len(questions) // n_sets + (1 if len(questions) % n_sets > i else 0):
                target_set = i
                break
        
        # Если не найден подходящий набор, просто добавляем в первый попавшийся (должно случаться редко)
        if target_set is None:
            target_set = min((len(test_sets[i]), i) for i in range(n_sets))[1]
        
        # Добавляем вопрос в целевой набор
        test_sets[target_set].append(question)
        # Обновляем счетчик тем
        theme_counts[question.theme] += 1

    return test_sets

# Пример использования
questions = [
    Question("Q1", Theme.MATH),
    Question("Q2", Theme.SCIENCE),
    Question("Q3", Theme.HISTORY),
    Question("Q4", Theme.LITERATURE),
    Question("Q5", Theme.MATH),
    Question("Q6", Theme.SCIENCE),
    # Добавьте больше вопросов по нуждам
]

# Распределяем вопросы по двум наборам тестов
test_sets = distribute_questions(questions, 2)

# Выводим результат
for test_set, qs in test_sets.items():
    print(f"Test Set {test_set}: {[q.name for q in qs]}")
