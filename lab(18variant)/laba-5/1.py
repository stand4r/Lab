import tkinter as tk
from tkinter import ttk
from enum import Enum
from functools import cmp_to_key

# Перечисления для свойств абитуриентов и условий учебы
class Property(Enum):
    HIGH_GPA = 1
    LOW_GPA = -1
    HIGH_SAT = 1
    LOW_SAT = -1
    EXTRACURRICULARS = 1
    NO_EXTRACURRICULARS = -1

class Abiturient:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

class University:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties
        self.capacity = 2  # Допустим, каждый вуз может принять 10 студентов

# Функция для сравнения абитуриентов
def compare_abiturients(a, b):
    score_a = sum(a.properties[prop] for prop in a.properties)
    score_b = sum(b.properties[prop] for prop in b.properties)
    return score_b - score_a

# Функция для сравнения вузов
def compare_universities(a, b, abiturient):
    score_a = sum(a.properties[prop] for prop in a.properties if prop in abiturient.properties)
    score_b = sum(b.properties[prop] for prop in b.properties if prop in abiturient.properties)
    return score_b - score_a

# Пример данных
abiturients = [
    Abiturient("Student1", {Property.HIGH_GPA: 1, Property.HIGH_SAT: 1}),
    Abiturient("Student2", {Property.LOW_GPA: -1, Property.EXTRACURRICULARS: 1}),
    Abiturient("Student3", {Property.HIGH_GPA: 1, Property.LOW_SAT: -1}),
    Abiturient("Student4", {Property.HIGH_GPA: 1, Property.HIGH_SAT: 1, Property.EXTRACURRICULARS: 1}),
    Abiturient("Student5", {Property.LOW_GPA: -1, Property.LOW_SAT: -1}),
    Abiturient("Student6", {Property.HIGH_GPA: 1, Property.LOW_SAT: -1, Property.EXTRACURRICULARS: 1}),
]

universities = [
    University("Пгути", {Property.HIGH_GPA: 1, Property.EXTRACURRICULARS: 1}),
    University("СамГУПС", {Property.LOW_GPA: -1, Property.HIGH_SAT: 1}),
    University("СГЭУ", {Property.HIGH_GPA: 1, Property.LOW_SAT: -1}),
]

# Сортировка абитуриентов
sorted_abiturients = sorted(abiturients, key=cmp_to_key(compare_abiturients))

# Распределение абитуриентов по вузам
allocation = {}
for abiturient in sorted_abiturients:
    sorted_universities = sorted(universities, key=cmp_to_key(lambda a, b: compare_universities(a, b, abiturient)))
    for university in sorted_universities:
        if university.name not in allocation:
            allocation[university.name] = []
        if len(allocation[university.name]) < university.capacity:
            allocation[university.name].append(abiturient.name)
            break

# Графический интерфейс
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Абитуриенты и ВУЗы")
        self.geometry("800x400")

        self.left_frame = ttk.Frame(self)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.right_frame = ttk.Frame(self)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.university_listbox = tk.Listbox(self.left_frame)
        self.university_listbox.pack(fill=tk.Y, expand=True)
        self.university_listbox.bind('<<ListboxSelect>>', self.on_university_select)

        for university in universities:
            self.university_listbox.insert(tk.END, university.name)

        self.tree = ttk.Treeview(self.right_frame, columns=("Абитуриенты",))
        self.tree.heading("#0", text="Абитуриенты")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def on_university_select(self, event):
        selected_index = self.university_listbox.curselection()
        if not selected_index:
            return

        selected_university = self.university_listbox.get(selected_index)
        self.tree.delete(*self.tree.get_children())

        for abiturient in allocation.get(selected_university, []):
            self.tree.insert("", "end", text=abiturient)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
