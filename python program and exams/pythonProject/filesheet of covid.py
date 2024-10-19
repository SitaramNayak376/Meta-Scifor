import tkinter as tk
from tkinter import messagebox



def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    address = text_address.get("1.0", tk.END)
    email = entry_email.get()
    contact = entry_contact.get()
    country = entry_country.get()
    state = entry_state.get()
    diseases = []
    if var_cold.get():
        diseases.append("Cold")
    if var_cough.get():
        diseases.append("Cough")
    if var_fever.get():
        diseases.append("Fever")
    if var_headache.get():
        diseases.append("Headache")
    messagebox.showinfo("Registration Info",
    f"Name: {name}\nAge: {age}\nGender: {gender}\nAddress: {address.strip()}\n"
                        f"Email: {email}\nContact No: {contact}\nCountry: {country}\nState: {state}\n"
                        f"Diseases: {', '.join(diseases)}")



root = tk.Tk()
root.title("COVID Vaccine Registration Form")

tk.Label(root, text="Name:").grid(row=0, column=0, sticky=tk.W, pady=2)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, pady=2)

tk.Label(root, text="Age:").grid(row=1, column=0, sticky=tk.W, pady=2)
entry_age = tk.Entry(root, width=30)
entry_age.grid(row=1, column=1, pady=2)

tk.Label(root, text="Gender:").grid(row=2, column=0, sticky=tk.W, pady=2)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky=tk.W)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, sticky=tk.W)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").grid(row=2, column=3, sticky=tk.W)

tk.Label(root, text="Address:").grid(row=3, column=0, sticky=tk.W, pady=2)
text_address = tk.Text(root, width=30, height=3)
text_address.grid(row=3, column=1, pady=2)

tk.Label(root, text="Email ID:").grid(row=4, column=0, sticky=tk.W, pady=2)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=4, column=1, pady=2)

tk.Label(root, text="Contact No:").grid(row=5, column=0, sticky=tk.W, pady=2)
entry_contact = tk.Entry(root, width=30)
entry_contact.grid(row=5, column=1, pady=2)

tk.Label(root, text="Country:").grid(row=6, column=0, sticky=tk.W, pady=2)
entry_country = tk.Entry(root, width=30)
entry_country.grid(row=6, column=1, pady=2)

tk.Label(root, text="State:").grid(row=7, column=0, sticky=tk.W, pady=2)
entry_state = tk.Entry(root, width=30)
entry_state.grid(row=7, column=1, pady=2)

tk.Label(root, text="Select if you have any of the following diseases:").grid(row=8, column=0, columnspan=2,
                                                                              sticky=tk.W, pady=2)
var_cold = tk.BooleanVar()
tk.Checkbutton(root, text="Cold", variable=var_cold).grid(row=9, column=0, sticky=tk.W)
var_cough = tk.BooleanVar()
tk.Checkbutton(root, text="Cough", variable=var_cough).grid(row=9, column=1, sticky=tk.W)
var_fever = tk.BooleanVar()
tk.Checkbutton(root, text="Fever", variable=var_fever).grid(row=9, column=2, sticky=tk.W)
var_headache = tk.BooleanVar()
tk.Checkbutton(root, text="Headache", variable=var_headache).grid(row=9, column=3, sticky=tk.W)
tk.Button(root, text="Submit", command=submit_form).grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
