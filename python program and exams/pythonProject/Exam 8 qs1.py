import tkinter as tk
from functools import partial
def filter_strings(char, case_sensitive):
    strings = ["Apple", "banana", "Cherry", "Date", "fig", "Grape"]

    if not case_sensitive:
        char = char.lower()
        strings = [s.lower() for s in strings]

    filtered_strings = list(filter(lambda x: char in x, strings))

    result_label.config(text=f"Strings containing '{char}': {filtered_strings}")



def on_filter_click():
    char = char_entry.get()
    case_sensitive = case_var.get()

    filter_strings(char, case_sensitive)


root = tk.Tk()
root.title("Advanced String Filter")

tk.Label(root, text="Enter character to filter:").pack(pady=5)
char_entry = tk.Entry(root)
char_entry.pack(pady=5)

case_var = tk.BooleanVar(value=True)
case_check = tk.Checkbutton(root, text="Case Sensitive", variable=case_var)
case_check.pack(pady=5)

filter_button = tk.Button(root, text="Filter Strings", command=on_filter_click)
filter_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()