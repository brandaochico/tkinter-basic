import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Tabs')

# notebook para guardar as diferentes abas
notebook = ttk.Notebook(window)

## aba 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text= 'Texto na Aba 1')
label1.pack()

notebook.add(tab1, text= 'Aba 1')

## aba 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text= 'Texto na Aba 2')
label2.pack()

notebook.add(tab2, text= 'Aba 2')

notebook.pack()

window.mainloop()
