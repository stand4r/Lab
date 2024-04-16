from enum import Enum
from collections import defaultdict

# Определение перечисления для тематик книг
class Theme(Enum):
    FICTION = "Fiction"
    NONFICTION = "Non-fiction"
    SCIENCE = "Science"
    HISTORY = "History"
    CHILDREN = "Children"

# Класс книги
class Book:
    def __init__(self, author, title, theme):
        self.author = author
        self.title = title
        self.theme = theme

    def __repr__(self):
        return f"{self.author}: '{self.title}' [{self.theme.value}]"

# Класс для создания наборов книг
class BookCollector:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    # Функция для распределения книг по наборам
    def distribute_books(self, n):
        # Сортировка книг по авторам
        sorted_books = sorted(self.books, key=lambda x: x.author)
        
        # Создание словаря для наборов
        sets = defaultdict(list)
        
        # Распределение книг по наборам
        for i, book in enumerate(sorted_books):
            sets[i % n].append(book)
        
        return sets

# --- Пример использования ---
# Создание коллектора
collector = BookCollector()

# Добавление книг
collector.add_book(Book("Tolkien", "The Hobbit", Theme.FICTION))
collector.add_book(Book("Hawking", "A Brief History of Time", Theme.SCIENCE))
collector.add_book(Book("Dahl", "Matilda", Theme.CHILDREN))
collector.add_book(Book("Sagan", "Cosmos", Theme.SCIENCE))

# Создание 2 наборов книг
book_sets = collector.distribute_books(int(input("Количество наборов: ")))

# Вывод наборов книг
for set_number, books in book_sets.items():
    print(f"Набор {set_number + 1}:")
    for book in books:
        print(book)
    print()
