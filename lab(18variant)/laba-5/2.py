#Вариант 18
import tkinter as tk
from tkinter import ttk

class TaylorSeries:
    @staticmethod
    def ln_series(x):
        result = 0
        term = x - 1
        n = 1
        while n <= 10:  
            result += term / (n * x**n)
            term *= (x - 1) / x
            n += 1
        return result

def calculate():
    try:
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())
        delta_x = float(entry_delta_x.get())

        table = []
        x = x1
        while x <= x2:
            taylor_result = TaylorSeries.ln_series(x)
            table.append((x, taylor_result))
            x += delta_x

        for row in table:
            tree.insert("", "end", values=row)
    except ValueError:
        result_label.config(text="Пожалуйста, введите корректные значения", fg="red")

root = tk.Tk()
root.title("Вычисление ln(x)")
root.geometry("600x400")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

label_x1 = ttk.Label(frame, text="x1:")
label_x1.grid(row=0, column=0, padx=5, pady=5)
entry_x1 = ttk.Entry(frame)
entry_x1.grid(row=0, column=1, padx=5, pady=5)

label_x2 = ttk.Label(frame, text="x2:")
label_x2.grid(row=1, column=0, padx=5, pady=5)
entry_x2 = ttk.Entry(frame)
entry_x2.grid(row=1, column=1, padx=5, pady=5)

label_delta_x = ttk.Label(frame, text="Δx:")
label_delta_x.grid(row=2, column=0, padx=5, pady=5)
entry_delta_x = ttk.Entry(frame)
entry_delta_x.grid(row=2, column=1, padx=5, pady=5)

calculate_button = ttk.Button(frame, text="Рассчитать", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(frame, text="", foreground="red")
result_label.grid(row=4, column=0, columnspan=2)

columns = ("x", "Функция (ряд Тейлора)")
tree = ttk.Treeview(frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

root.mainloop()
