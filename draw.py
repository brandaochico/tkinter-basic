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

def adjust_brush_size(event):
    global brush_size
    
    if event.num == 4:
        brush_size += 2
    else:
        brush_size -= 2

    brush_size = max(0, min(brush_size,10))
    print(event)


def on_mousewheel(widget, func, prefix='Any'):
    widget.bind(f'<{prefix}-Button-4>', func)
    widget.bind(f'<{prefix}-Button-5>', func)


brush_size = 4
canvas.bind('<Motion>', draw_on_canvas)
on_mousewheel(canvas, adjust_brush_size)

window.mainloop()
