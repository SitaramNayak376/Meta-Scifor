import tkinter as tk
from tkinter import messagebox

students = []
def register_student():
    name = name_entry.get()
    age = int(age_entry.get())
    grade = grade_entry.get()
    gender = gender_var.get()

    if name and age and grade:
        students.append({"name": name, "age": age, "grade": grade, "gender": gender})
        messagebox.showinfo("Success", "Student {name} registered successfully!")
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")



def filter_students():
    min_age = int(min_age_entry.get())
    grade_to_filter = filter_grade_entry.get()

    filtered_students = list(filter(lambda x: x['age'] > min_age and x['grade'] == grade_to_filter, students))

    result_text = "Filtered Students:\n"
    for student in filtered_students:
        result_text += "Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Gender: {student['gender']}\n"

    result_label.config(text=result_text)

root = tk.Tk()
root.title("School Registration Form")

tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Grade:").grid(row=2, column=0)
grade_entry = tk.Entry(root)
grade_entry.grid(row=2, column=1)

tk.Label(root, text="Gender:").grid(row=3, column=0)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky="W")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=3, column=2, sticky="W")

submit_button = tk.Button(root, text="Submit", command=register_student)
submit_button.grid(row=4, column=1)

tk.Label(root, text="Filter by Minimum Age:").grid(row=5, column=0)
min_age_entry = tk.Entry(root)
min_age_entry.grid(row=5, column=1)

tk.Label(root, text="Filter by Grade:").grid(row=6, column=0)
filter_grade_entry = tk.Entry(root)
filter_grade_entry.grid(row=6, column=1)

filter_button = tk.Button(root, text="Filter Students", command=filter_students)
filter_button.grid(row=7, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=8, column=0, columnspan=3)
root.mainloop()