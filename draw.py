import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title('Paint!')

canvas = tk.Canvas(window, bg= 'white')
canvas.pack()

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(
        (
            x - brush_size / 2,
            y - brush_size / 2,
            x + brush_size / 2,
            y + brush_size / 2,
        ),
        fill= 'black'
    )

brush_size = 4
canvas.bind('<Motion>', draw_on_canvas)

window.mainloop()
