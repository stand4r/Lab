# Вариант 3
import tkinter as tk

is_prime = lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 2)) and x > 1

def display_primes():
    text.delete("1.0", tk.END)
    
    primes = [num for num in range(2, 101) if is_prime(num)]
    text.insert(tk.END, "лямбда выражение генерируещие простые числа от 2 до 100:\n")
    for prime in primes:
        text.insert(tk.END, f"{prime}\n")

root = tk.Tk()
root.title("Простые числа")

text = tk.Text(root, height=10, width=30)
text.grid(row=0, column=0, padx=10, pady=10)

button_display = tk.Button(root, text="Вывести простые числа", command=display_primes)
button_display.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
