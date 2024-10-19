import tkinter as tk
import math


class ScientificCalc:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.root.configure(bg='red')

        self.display = tk.Entry(root, font=("Arial", 30), borderwidth=10, relief="groove", bg='white')
        self.display.grid(row=0, column=0, columnspan=5, pady=10)

        self.create_widgets()

    def create_widgets(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('log', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('*2', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('*3', 3, 4),
            ('0', 4, 1), ('.', 4, 0), ('+', 4, 3), ('=', 4, 2), ('AC', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sec', 5, 3), ('cosec', 5, 4),
            ('cot', 6, 0), ('(', 6, 1), (')', 6, 2),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=7, height=2, font=("Arial", 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.display.get()
                result = eval(expression, {"__builtins__": None}, {"math": math})
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == 'AC':
            self.display.delete(0, tk.END)
        elif char == 'log':
            try:
                value = float(self.display.get())
                result = math.log10(value)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == '*2':
            try:
                value = float(self.display.get())
                result = value * 2
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == '*3':
            try:
                value = float(self.display.get())
                result = value * 3
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, char)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalc(root)
    root.mainloop()
