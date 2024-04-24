# Вариант 3
import tkinter as tk
from tkinter import ttk

def flArr():
    n = int(n_entry.get())
    m = int(m_entry.get())

    for i in range(n):
        values = [(j + i) % m for j in range(m)]
        grid.insert("", "end", values=values)

root = tk.Tk()
root.title("Заполнение массива через DataGridView")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

n_label = ttk.Label(frame, text="Введите n:")
n_label.grid(row=0, column=0, padx=5, pady=5)
n_entry = ttk.Entry(frame)
n_entry.grid(row=0, column=1, padx=5, pady=5)

m_label = ttk.Label(frame, text="Введите m:")
m_label.grid(row=1, column=0, padx=5, pady=5)
m_entry = ttk.Entry(frame)
m_entry.grid(row=1, column=1, padx=5, pady=5)

fill_button = ttk.Button(frame, text="Заполнить массив", command=flArr)
fill_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

columns = [str(i) for i in range(6)]
grid = ttk.Treeview(frame, columns=columns, show="headings")
for col in columns:
    grid.heading(col, text=col)
grid.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
