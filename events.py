''' https://www.pythontutorial.net/tkinter/tkinter-event-binding/ '''

import tkinter as tk
from tkinter import ttk

# janela
window = tk.Tk()
window.geometry('600x500')
window.title('Eventos')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text= 'Botão')
button.pack()

# events
def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

window.bind('<Alt-KeyPress-a>', lambda event: print('apertou Alt+A'))
window.bind('<KeyPress>', lambda event: print('uma tecla foi apertada'))

text.bind('<Motion>', get_pos)

entry.bind('<FocusIn>', lambda event: print('entry field foi selecionada'))
entry.bind('<FocusOut>', lambda event: print('entry field foi desselecionada'))

## no Linux, <MouseWheel> não funciona
## o jeito mais apropriado de fazer seria:
def on_mousewheel(widget, func, prefix='Any'):
    widget.bind(f'<{prefix}-Button-4>', func)
    widget.bind(f'<{prefix}-Button-5>', func)

## e chamar assim:
on_mousewheel(text, lambda event: print('scroll do mouse utilizado'))

window.mainloop()

