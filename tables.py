import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.geometry('600x400')
window.title('TreeView')


# data
first_names = ['Maria', 'Ana', 'Francisca', 'Julia', 'Antonia', 'José', 'João', 'Antonio', 'Francisco', 'Pedro']
last_names = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Ferreira', 'Lima', 'Alves', 'Rodrigues', 'Costa']
emails_ext = ['gmail.com', 'hotmail.com', 'outlook.com', 'uol.com.br', 'terra.com.br']

# treeview
table = ttk.Treeview(
    window,
    columns= ('nome', 'sobrenome', 'email'),
    show= 'headings'
)

for column in table['columns']:
    table.heading(column, text= column.capitalize())

table.pack(fill= 'both', expand= True)

# inserir valores na tabela
for i in range(50):
    first_name = choice(first_names)
    last_name = choice(last_names)
    email = f'{first_name.lower()}{last_name.lower()}@{choice(emails_ext)}'

    table.insert(
        parent= '',
        index= 0,
        values= (first_name, last_name, email)
    )

# eventos em tabelas
## seleção de itens
def item_select(_):
    for i in table.selection():
        print(table.item(i)['values'])

table.bind('<<TreeviewSelect>>', item_select)

## remoção de itens
def delete_items(_):
    for i in table.selection():
        table.delete(i)

table.bind('<Delete>', delete_items)

window.mainloop()
