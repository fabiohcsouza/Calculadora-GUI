import tkinter as tk
from typing import List
import re
import math

class Calculator:
    """teste"""
    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry, buttons: List[list[tk.Button]]):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons
    
    def start(self):
        self._config_buttons()
        self._config_display()
        self.root.mainloop()
    
    def _config_buttons(self):
        buttons = self.buttons
        for row in buttons:
            for button in row:
                button_text = button['text']

                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)
                    button.config(bg='#EA4335', fg='#fff')
                
                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)
                
                if button_text == '=':
                    button.bind('<Button-1>', self.calculate)
                    button.config(bg='#4785F4', fg='#fff')
                    


    def _config_display(self):
        self.display.bind('<Return>', lambda e: self.calculate())
        self.display.bind('<KP_Enter>', self.calculate)

    def _fix_text(self, text):
        # Substitui tudo que não é 0123456789.+-/*()^ para nada
        text = re.sub(r'[^\d\.\/\*\+\-\(\)\^e]', r'', text, 0)
        # Substitui sinais repetidos para 1 sinal
        text = re.sub(r'([\.\+\-\*\/\^])\1+', r'\1', text, 0)
        # Substitui () ou *() para nada
        text = re.sub(r'\*?\(\)', '', text)

        return text

    def clear(self, event=None):
        self.display.delete(0, 'end')

    def add_text_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])
    
    def calculate(self, event=None):
        fixed_text = self._fix_text(self.display.get())
        equations = self._get_equations(fixed_text)
        
        try:
            if len(equations) == 1:
                result = eval(self._fix_text(equations[0]))
            else:
                result = eval(self._fix_text(equations[0]))
                for equation in equations[:1]:
                    result = math.pow(result, eval(self._fix_text(equation)))
            
            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text=f'{fixed_text} = {result}')
        
        except OverflowError:
            self.label.config(text="I couldn't do the math, sorry")
        except Exception:
            self.label.config(text='Invalid account')

    def _get_equations(self, text):
        return re.split(r'\^', text, 0)