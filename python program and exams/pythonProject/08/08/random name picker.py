import tkinter as tk
import random

class RandomNamePicker:
    def __init__(self,root):
        self.root = root
        self.root.title("Random Name Picker")

        self.students = ["sitaram","ram","sita","gita", "mita","shivansh","babu"]
        self.completed = []

        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side= tk.LEFT,padx=20,pady=20)

        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side=tk.RIGHT,padx=20,pady=20)

        self.label_remaining = tk.Label(self.left_frame,text = "Remaining Names", font=("Helvetica", 16))
        self.label_remaining.pack(pady=10)

        self.remaining_listbox = tk.Listbox(self.left_frame, width=30,height=10,font=("Helvetica",14))
        self.remaining_listbox.pack(pady=10)
        for student in self.students:
            self.remaining_listbox.insert(tk.END,student)

        self.pick_button = tk.Button(self.left_frame, text= "Pick a Random Number", command = self.pick_name, font=("Helvetica",14))
        self.pick_button.pack(pady=20)

        self.label_selected = tk.Label(self.left_frame,text="Select Name:", font=("Helvetica",16))
        self.label_selected.pack(pady=10)

        self.selected_name = tk.Label(self.left_frame,text="", font=("Helvetica",24,"bold"),fg="blue")
        self.selected_name.pack(pady=10)

        self.label_completed = tk.Label(self.right_frame, text = "Picked Names", font=("Helvetica", 16))

        self.label_completed.pack(pady=10)

        self.completed_listbox = tk.Listbox(self.right_frame,width = 30, height = 10, font =("Helvetica", 14))
        self.completed_listbox.pack(pady=10)

    def pick_name(self):
        if self.students:
            name = random.choice(self.students)
            self.students.remove(name)
            self.completed.append(name)

            self.selected_name.config(text = name)
            self.remaining_listbox.delete(0,tk.END)
            for student in self.students:
                self.remaining_listbox.insert(tk.END,student)
            self.completed_listbox.insert(tk.END,name)
        else:
            self.selected_name.config(text = "No More Names")


if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNamePicker(root)
    root.mainloop()