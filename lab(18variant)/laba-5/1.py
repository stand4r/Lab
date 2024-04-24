#Вариант 3
import tkinter as tk
from tkinter import ttk

class ArrayApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Array App")

        self.array = [[0 for _ in range(6)] for _ in range(5)]

        self.create_wid()

    def create_wid(self):
        self.row_label = ttk.Label(self, text="Row:")
        self.row_entry = ttk.Entry(self)
        self.column_label = ttk.Label(self, text="Column:")
        self.column_entry = ttk.Entry(self)
        self.value_label = ttk.Label(self, text="Value:")
        self.value_entry = ttk.Entry(self)
        self.add_button = ttk.Button(self, text="Add", command=self.addArr)
        self.data_grid = ttk.Treeview(self, columns=[f"Column {i}" for i in range(1, 7)])

        self.data_grid.heading("#0", text="Row")
        for i in range(1, 7):
            self.data_grid.heading(f"Column {i}", text=f"Column {i}")

        self.row_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.row_entry.grid(row=0, column=1, padx=5, pady=5)
        self.column_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.column_entry.grid(row=1, column=1, padx=5, pady=5)
        self.value_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.value_entry.grid(row=2, column=1, padx=5, pady=5)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.data_grid.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def addArr(self):
        try:
            row = int(self.row_entry.get())
            column = int(self.column_entry.get())
            value = int(self.value_entry.get())

            if 0 <= row < 5 and 0 <= column < 6:
                self.array[row][column] = value
                self.update_data_grid()
            else:
                tk.messagebox.showerror("Error", "Row or column out of range")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid value")

    def newDG(self):
        self.data_grid.delete(*self.data_grid.get_children())
        for i, row in enumerate(self.array):
            self.data_grid.insert("", "end", text=f"Row {i}", values=row)


app = ArrayApp()
app.mainloop()
