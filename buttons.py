import tkinter as tk
from tkinter import ttk

window = tk.Tk();
window.title('Botões')
window.geometry('600x400')


# botão padrão
def button_func():
    print('botão apertado')

button_string = tk.StringVar(value= 'Botão com uma StringVar')
button = ttk.Button(window, command= button_func, textvariable= button_string)
button.pack()


# botão padrão chamando função com parâmetros
def button_func_with_params(param):
    print('botão com parâmetros foi apertado')
    print('param: ', param.get())

button_param = tk.StringVar(value= 'test')
button_with_params = ttk.Button(
    window, 
    text= 'botão com parâmetros!',
    command= lambda: button_func_with_params(button_param)
)
button_with_params.pack()


# botão checkbox
check_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(
    window, 
    text= 'checkbox', 
    command= lambda: print(check_var.get()),
    variable= check_var,
    onvalue= True,
    offvalue= False
)
checkbox.pack()


# botão radio
## botões radio SEMPRE necessitam de um value
radio_var = tk.StringVar();
radio1 = ttk.Radiobutton(
    window, 
    text= 'Radiobutton 1', 
    value= 'radio 1',
    variable= radio_var,
    command= lambda: print(radio_var.get())
)
radio1.pack()

radio2 = ttk.Radiobutton(
    window, 
    text= 'Radiobutton 2', 
    value= 2,
    variable= radio_var,
    command= lambda: print(radio_var.get())
)
radio2.pack()


window.mainloop()
