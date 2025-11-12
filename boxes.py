import tkinter as tk
from tkinter import ttk

# janela
window = tk.Tk()
window.geometry('600x500')
window.title('Caixas')

# combobox /// dropdown menu
items = ('Bulbasaur', 'Squirtle', 'Charmander')
selected = tk.StringVar(value= items[0])

combo = ttk.Combobox(window, textvariable= selected)
combo['values'] = items
combo.pack()

combo_label = ttk.Label(window, text= f'Selecionado: {selected.get()}')
combo_label.pack()

# evento com combobox
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text= f'Selecionado: {selected.get()}'))


# spinbox
spin_int = tk.IntVar(value= 5)
spin = ttk.Spinbox(
    window, 
    from_= 5, 
    to= 10,
    command= lambda: print(spin_int.get()),
    textvariable= spin_int
)

# eventos com spinbox
spin.bind('<<Increment>>', lambda event: print('o número foi aumentado'))
spin.bind('<<Decrement>>', lambda event: print('o número foi diminuído'))

spin.pack()

window.mainloop()
