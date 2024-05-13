import tkinter as tk
from tkinter import messagebox
import time
import math

class TaylorSeriesCalculator:
    def init(self):
        pass

    def calculate_cosine(self, x, epsilon):
        sum = 0
        n = 0
        term = 1  # Начальный член ряда равен 1, что правильно для 0-го элемента (чётные степени).

        while abs(term) > epsilon:
            sum += term
            term *= -x * x / ((2 * n + 1) * (2 * n + 2))
            n += 1

        return sum, n

    def calculate_cosine_with_stats(self, x, epsilon):
        sum, n = self.calculate_cosine(x, epsilon)
        math_cos = math.cos(x)
        difference = abs(sum - math_cos)

        return sum, math_cos, difference, n

class TaylorSeriesCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Taylor Series Calculator")

        self.x1_label = tk.Label(root, text="1x:")
        self.x1_label.grid(row=0, column=0)
        self.x1_entry = tk.Entry(root)
        self.x1_entry.grid(row=0, column=1)

        self.x2_label = tk.Label(root, text="2x:")
        self.x2_label.grid(row=1, column=0)
        self.x2_entry = tk.Entry(root)
        self.x2_entry.grid(row=1, column=1)

        self.delta_x_label = tk.Label(root, text="xΔ:")
        self.delta_x_label.grid(row=2, column=0)
        self.delta_x_entry = tk.Entry(root)
        self.delta_x_entry.grid(row=2, column=1)

        self.epsilon_label = tk.Label(root, text="ε:")
        self.epsilon_label.grid(row=3, column=0)
        self.epsilon_entry = tk.Entry(root)
        self.epsilon_entry.grid(row=3, column=1)

        self.calculate_button = tk.Button(root, text="Рассчитать", command=self.calculate)
        self.calculate_button.grid(row=4, column=0, columnspan=2)

        self.result_text = tk.Text(root)
        self.result_text.grid(row=5, column=0, columnspan=2)

    def calculate(self):
        try:
            x1 = float(self.x1_entry.get())
            x2 = float(self.x2_entry.get())
            delta_x = float(self.delta_x_entry.get())
            epsilon = float(self.epsilon_entry.get())

            calculator = TaylorSeriesCalculator()
            start_time = time.time()

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.INSERT, "  Argument\t  Taylor Series\t  Math.Cos\t  Difference\t  Terms\n")

            for x in range(int((x2 - x1) / delta_x) + 1):
                x_value = x1 + x * delta_x
                sum, math_cos, difference, n = calculator.calculate_cosine_with_stats(x_value, epsilon)
                self.result_text.insert(tk.INSERT, f"{round(x_value, 2):>10}\t{round(sum, 2):>15}\t{round(math_cos, 2):>10}\t{round(difference, 2):>12}\t{n:>7}\n")

            end_time = time.time()
            messagebox.showinfo("Calculation Time", f"Calculation took {end_time - start_time:.2f} seconds")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaylorSeriesCalculatorApp(root)
    root.mainloop()