import tkinter as tk
import ttkbootstrap as ttk

# funcionalidade
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61

    output_string.set(km_output)

# janela
window = ttk.Window(themename= 'journal')
window.title('Demo')
window.geometry('500x300')

# widget de título
title_label = ttk.Label(master= window, text= 'Milhas para Quilômetros', font= 'Calibri 24 bold')
title_label.pack()

# widget campo de input
input_frame = ttk.Frame(master= window)

entry_int = tk.IntVar()
entry = ttk.Entry(master= input_frame, textvariable= entry_int)
button = ttk.Button(master= input_frame, text= 'Converter', command= convert)

entry.pack(side= 'left', padx= 10)
button.pack(side= 'left')

input_frame.pack(pady= 10)

# widget de output
output_string = tk.StringVar()
output_label = ttk.Label(
    master= window, 
    text= 'Output', 
    font= 'Calibri 20', 
    textvariable= output_string
)
output_label.pack(pady= 5)

# executar
window.mainloop()
