import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.color = "black"
        self.eraser_color = "white"
        self.pen_size = 4
        self.eraser_mode = False

        self.create_widgets()
        self.setup_bindings()

    def create_widgets(self):
        self.pen_button = tk.Button(self.root, text="pen", command=self.use_pen)
        self.pen_button.grid(row=0, column=0, sticky=tk.W)

        self.brush_button = tk.Button(self.root, text="brush", command=self.use_brush)
        self.brush_button.grid(row=1, column=0, sticky=tk.W)

        self.color_button = tk.Button(self.root, text="color", command=self.choose_color)
        self.color_button.grid(row=2, column=0, sticky=tk.W)

        self.eraser_button = tk.Button(self.root, text="eraser", command=self.use_eraser)
        self.eraser_button.grid(row=3, column=0, sticky=tk.W)

        self.pen_size_slider = tk.Scale(self.root, from_=1, to=10, orient=tk.HORIZONTAL)
        self.pen_size_slider.grid(row=4, column=0, sticky=tk.W)
        self.pen_size_slider.set(self.pen_size)



        self.canvas = tk.Canvas(self.root, bg="white", width=500, height=400)
        self.canvas.grid(row=0, column=1, rowspan=6)

    def setup_bindings(self):
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def use_pen(self):
        self.eraser_mode = False

    def use_brush(self):
        self.eraser_mode = False

    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def use_eraser(self):
        self.eraser_mode = True

    def paint(self, event):
        self.pen_size = self.pen_size_slider.get()
        x1, y1 = (event.x - self.pen_size), (event.y - self.pen_size)
        x2, y2 = (event.x + self.pen_size), (event.y + self.pen_size)

        if self.eraser_mode:
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.eraser_color, outline=self.eraser_color)
        else:
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def reset(self, event):
        self.old_x, self.old_y = None, None

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()