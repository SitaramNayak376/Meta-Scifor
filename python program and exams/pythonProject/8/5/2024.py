import tkinter as tk
from tkinter import messagebox
import json


questions_json = '''
[
    {
        "question": "What is the capital of india?",
        "options": ["Berlin", "Delhi", "Paris", "Rome"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },
    {
        "question": "What is the largest lake in world?",
        "options": ["caspian sea","baikal","lake superior","ontario"],
        "answer": "baikal"
    }
]
'''


questions = json.loads(questions_json)


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=700, font=("Arial", 14))
        self.question_label.pack(pady=30)

        self.var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 14))
            rb.pack(anchor=tk.W)
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        question_data = questions[self.question_index]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.radio_buttons[i].config(text=option, value=option)
        self.var.set(None)

    def next_question(self):
        selected_option = self.var.get()
        if selected_option == questions[self.question_index]["answer"]:
            self.score += 1
        self.question_index += 1
        if self.question_index < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Your score: {self.score}/{len(questions)}")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()