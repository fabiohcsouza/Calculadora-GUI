import tkinter as tk
from typing import List

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculator')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root

def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text='No accounts',
        anchor='e', justify='right', background='#fff' #anchor=widget
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10)) #columnspan=ate onde vai, sticky=rxpandir, etc, 
    display.config(
        font=('Helvetica', 40, 'bold'), #fonte= font, tam, gro
        justify='right', bd=1, relief='flat', #justify=letra, bd=borda, relief=fundo
        highlightthickness=1, highlightcolor='#ccc'
        )
    display.bind('<Control-a>', _display_control_a) #Cria evento para usar Ctrl+a
    return display

def _display_control_a(event):
    event.widget.select_range(0, 'and') #Seleciona tudo dento do display
    event.widget.icursor('end') #move curso para end
    return 'break'

def make_buttons(root) -> List[list[tk.Button]]:
    button_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    buttons: List[list[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(row=row, column=col_index, sticky='news', padx=5, pady=5) #pady,x = espaço entre btn
            btn.config(
                font=('Helvetica', 15, 'normal'),
                pady=40, width=1, background='#f1f2f3', bd=0,
                cursor='hand2', highlightthickness=0, highlightcolor='#ccc', highlightbackground='#ccc', 
                activebackground='#ccc'
            )
            button_row.append(btn)
        buttons.append(button_row)  
    return buttons


