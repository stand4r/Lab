# Вариант 3
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import random

class СписокМассива:
    def __init__(self):
        self._данные = []

    def add(self, значение):
        self._данные.append(значение)

    def add_to_index(self, индекс, значение):
        self._данные.insert(индекс, значение)

    def resize_hg(self, новый_размер):
        if новый_размер >= len(self._данные):
            self._данные.extend([0] * (новый_размер - len(self._данные)))
        else:
            self._данные = self._данные[:новый_размер]

    def det_elem(self):
        return self._данные

class Делегат:
    @staticmethod
    def find_max(список_массива):
        if not список_массива:
            return None
        return max(список_массива)

    @staticmethod
    def find_min(список_массива):
        if not список_массива:
            return None
        return min(список_массива)

    @staticmethod
    def fiind_avrg(список_массива):
        if not список_массива:
            return None
        return sum(список_массива) / len(список_массива)

    @staticmethod
    def find_sum(список_массива):
        if not список_массива:
            return None
        return sum(список_массива)

class Приложение:
    def __init__(self, master):
        self.master = master
        self.список_массива = СписокМассива()

        self.label = tk.Label(master, text="Демонстрация Списка Массива", font=("Arial", 18))
        self.label.pack()

        self.text_area = scrolledtext.ScrolledText(master, width=40, height=10)
        self.text_area.pack()

        self.add_button = tk.Button(master, text="Добавить Случайный Элемент", command=self.add_random_element)
        self.add_button.pack()

        self.addAtind_frame = tk.Frame(master)
        self.addAtind_frame.pack()
        tk.Label(self.addAtind_frame, text="Индекс:").grid(row=0, column=0)
        tk.Label(self.addAtind_frame, text="Значение:").grid(row=0, column=2)
        self.index_entry = tk.Entry(self.addAtind_frame)
        self.index_entry.grid(row=0, column=1)
        self.value_entry = tk.Entry(self.addAtind_frame)
        self.value_entry.grid(row=0, column=3)
        self.addAtind_button = tk.Button(self.addAtind_frame, text="Добавить Элемент по Индексу", command=self.add_element_at_index)
        self.addAtind_button.grid(row=0, column=4)

        self.resize_frame = tk.Frame(master)
        self.resize_frame.pack()
        tk.Label(self.resize_frame, text="Новый Размер:").grid(row=0, column=0)
        self.new_size_entry = tk.Entry(self.resize_frame)
        self.new_size_entry.grid(row=0, column=1)
        self.resize_button = tk.Button(self.resize_frame, text="Изменить Размер Списка", command=self.resize_array_list)
        self.resize_button.grid(row=0, column=2)

        self.delegate_button = tk.Button(master, text="Делегировать Операции", command=self.delegate_operations)
        self.delegate_button.pack()

    def add_random_element(self):
        случайное_значение = random.uniform(0, 100)
        self.список_массива.add(случайное_значение)
        self.update_text_area()

    def add_element_at_index(self):
        try:
            индекс = int(self.index_entry.get())
            значение = float(self.value_entry.get())
            self.список_массива.add_to_index(индекс, значение)
            self.update_text_area()
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный ввод! Пожалуйста, введите корректный индекс и значение.")

    def resize_array_list(self):
        try:
            новый_размер = int(self.new_size_entry.get())
            self.список_массива.resize_hg(новый_размер)
            self.update_text_area()
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный ввод! Пожалуйста, введите корректный размер.")

    def delegate_operations(self):
        элементы = self.список_массива.det_elem()
        if not элементы:
            messagebox.show
