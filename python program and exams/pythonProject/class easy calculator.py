import tkinter as tk
window = tk.Tk()
window.title("CALCULATOR")
label1=tk.Label(window,text="",bg="red")
label1.pack()
label2=tk.Label(window,text="",bg="red")
label2.pack()
label3=tk.Label(window,text="",bg="red")
label3.pack()
label4=tk.Label(window,text="",bg="red")
label4.pack()
label5=tk.Label(window,text="",bg="red")
label5.pack()

def calc():
  a = 20
  b = 10
  x = a-b
  y= a+b
  z = a/b
  m = a%b
  n = a**b
  label1.config(text = x)
  label2.config(text=y)
  label3.config(text=z)
  label4.config(text=m)
  label5.config(text=n)

button = tk.Button(window,text="click",bg="green",command=calc)
button.pack()
window.mainloop()

