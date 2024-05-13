from enum import Enum

class Theme(Enum):
    MATH = 1
    PHYSICS = 2
    COMPUTER_SCIENCE = 3
    HISTORY = 4
    LITERATURE = 5

class Question:
    def __init__(self, name, theme):
        self.name = name
        self.theme = theme

def distribute_questions(questions, n):
    # Sort questions by name
    questions.sort(key=lambda x: x.name)

    # Initialize test sets
    test_sets = [[] for _ in range(n)]

    # Distribute questions to test sets
    for i, question in enumerate(questions):
        test_sets[i % n].append(question)

    return test_sets

# Example usage
questions = [
    Question("What is 2+2?", Theme.MATH),
    Question("What is the speed of light?", Theme.PHYSICS),
    Question("What is Python?", Theme.COMPUTER_SCIENCE),
    Question("Who was Napoleon?", Theme.HISTORY),
    Question("What is the meaning of life?", Theme.LITERATURE),
    Question("What is the derivative of x^2?", Theme.MATH),
    Question("What is the atomic mass of carbon?", Theme.PHYSICS),
    Question("What is the difference between Python 2 and 3?", Theme.COMPUTER_SCIENCE),
    Question("What was the Treaty of Versailles?", Theme.HISTORY),
    Question("What is the theme of To Kill a Mockingbird?", Theme.LITERATURE),
    Question("What is the Pythagorean theorem?", Theme.MATH),
    Question("What is Newton's second law?", Theme.PHYSICS),
    Question("What is object-oriented programming?", Theme.COMPUTER_SCIENCE),
    Question("Who was the first president of the United States?", Theme.HISTORY),
    Question("What is the plot of Pride and Prejudice?", Theme.LITERATURE),
]

n = int(input("Введите количество тестов: "))
test_sets = distribute_questions(questions, n)

for i, test_set in enumerate(test_sets):
    print(f"Test Set {i+1}:")
    for question in test_set:
        print(f"  {question.name} ({question.theme.name})")
    print()