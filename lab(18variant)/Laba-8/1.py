import random
import tkinter as tk

class DynamicArray:
    def __init__(self):
        self.array = []
        self.capacity = 30

    def add(self, index, value):
        if len(self.array) < self.capacity:
            self.array.insert(index, value)
        else:
            self.resize(self.capacity * 2)
            self.add(index, value)

    def add_multiple(self, values):
        for value in values:
            self.add(len(self.array), value)

    def add_to_beginning(self, values):
        for value in values:
            self.add(0, value)

    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def get_delegate(self):
        return Delegate(self.array)

class Delegate:
    def __init__(self, array):
        self.array = array

    def find_max(self):
        return max(self.array)

    def find_min(self):
        return min(self.array)

    def find_average(self):
        return sum(self.array) / len(self.array)

    def find_sum(self):
        return sum(self.array)

class DynamicArrayApp:
    def __init__(self, master):
        self.master = master
        self.dynamic_array = DynamicArray()
        self.delegate = self.dynamic_array.get_delegate()

        self.label_capacity = tk.Label(master, text="Емкость: 30")
        self.label_capacity.pack()

        self.label_size = tk.Label(master, text="Размер: 0")
        self.label_size.pack()

        self.label_values = tk.Label(master, text="Значения:")
        self.label_values.pack()

        self.text_values = tk.Text(master, height=10, width=70)
        self.text_values.pack()

        self.button_add = tk.Button(master, text="Добавить элемент", command=self.add_element)
        self.button_add.pack()

        self.button_add_multiple = tk.Button(master, text="Добавить несколько элементов", command=self.add_multiple_elements)
        self.button_add_multiple.pack()

        self.button_add_to_beginning = tk.Button(master, text="Добавить элементы в начало", command=self.add_to_beginning)
        self.button_add_to_beginning.pack()
        
        self.button_print = tk.Button(master, text="Вывести массив", command=self.print_array)
        self.button_print.pack()

        self.button_find_max = tk.Button(master, text="Найти максимум", command=self.find_max)
        self.button_find_max.pack()

        self.button_find_min = tk.Button(master, text="Найти минимум", command=self.find_min)
        self.button_find_min.pack()

        self.button_find_average = tk.Button(master, text="Найти среднее", command=self.find_average)
        self.button_find_average.pack()

        self.button_find_sum = tk.Button(master, text="Найти сумму", command=self.find_sum)
        self.button_find_sum.pack()
    
    def clear_entry_and_button(self, entry, button):
        entry.pack_forget()
        button.pack_forget()

    def print_array(self):
        self.text_values.config(state=tk.NORMAL)
        self.text_values.delete(1.0, tk.END)
        self.text_values.insert(tk.END, "{}".format(self.dynamic_array.array))
        self.text_values.config(state=tk.DISABLED)

    def add_element(self):
        value_entry = tk.Entry(self.master)
        value_entry.pack()
        value_entry.focus()
        value_button = tk.Button(self.master, text="Добавить", command=lambda: self.add_value(value_entry, value_button))
        value_button.pack()

    def add_value(self, entry, button):
        value = float(entry.get())
        self.dynamic_array.add(len(self.dynamic_array.array), value)
        self.clear_entry_and_button(entry, button)
        self.update_values()

    def add_multiple_elements(self):
        values_entry = tk.Entry(self.master)
        values_entry.pack()
        values_entry.focus()
        values_button = tk.Button(self.master, text="Добавить", command=lambda: self.add_multiple_values(values_entry, values_button))
        values_button.pack()

    def add_multiple_values(self, entry, button):
        values = [float(value) for value in entry.get().split()]
        self.dynamic_array.add_multiple(values)
        self.clear_entry_and_button(entry, button)
        self.update_values()

    def add_to_beginning(self):
        values_entry = tk.Entry(self.master)
        values_entry.pack()
        values_entry.focus()
        values_button = tk.Button(self.master, text="Добавить", command=lambda: self.add_multiple_values_to_beginning(values_entry, values_button))
        values_button.pack()

    def add_multiple_values_to_beginning(self, entry, button):
        values = [float(value) for value in entry.get().split()]
        self.dynamic_array.add_to_beginning(values)
        self.clear_entry_and_button(entry, button)
        self.update_values()

    def find_max(self):
        self.text_values.config(state=tk.NORMAL)
        self.text_values.delete(1.0, tk.END)
        max_value = self.delegate.find_max()
        self.text_values.insert(tk.END, "Максимальное значение: {}\n".format(max_value))
        self.text_values.config(state=tk.DISABLED)

    def find_min(self):
        self.text_values.config(state=tk.NORMAL)
        self.text_values.delete(1.0, tk.END)
        min_value = self.delegate.find_min()
        self.text_values.insert(tk.END, "Минимальное значение: {}\n".format(min_value))
        self.text_values.config(state=tk.DISABLED)

    def find_average(self):
        self.text_values.config(state=tk.NORMAL)
        self.text_values.delete(1.0, tk.END)
        average_value = self.delegate.find_average()
        self.text_values.insert(tk.END, "Среднее значение: {}\n".format(average_value))
        self.text_values.config(state=tk.DISABLED)

    def find_sum(self):
        self.text_values.config(state=tk.NORMAL)
        self.text_values.delete(1.0, tk.END)
        sum_value = self.delegate.find_sum()
        self.text_values.insert(tk.END, "Сумма значений: {}\n".format(sum_value))
        self.text_values.config(state=tk.DISABLED)

    def update_values(self):
        self.label_capacity.config(text="Емкость: {}".format(self.dynamic_array.capacity))
        self.label_size.config(text="Размер: {}".format(len(self.dynamic_array.array)))
        self.text_values.config(state=tk.NORMAL)
        self.text_values.delete(1.0, tk.END)
        for value in self.dynamic_array.array:
            self.text_values.insert(tk.END, "{} ".format(value))
        self.text_values.config(state=tk.DISABLED)

root = tk.Tk()
app = DynamicArrayApp(root)
root.mainloop()
