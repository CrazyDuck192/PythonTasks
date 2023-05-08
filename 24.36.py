"""24.36. Скласти програму з графічним інтерфейсом для 
реалізації простого калькулятора. Калькулятор повинен мати 
набір кнопок для введення цифр та арифметичних дій а також 
вікно для виведення результату як на рисунку нижче."""

from tkinter import *

class CalculatorGui:

    def __init__(self, form):
        self.equation = ''
        self.frame = form
        self.frame.title('Calculator')
        self.def_font = ('arial', 16)

        self.operators = ['C', '**', 'sqrt', '/', '*', '+', '-']
        self.symbs = ['C', '^', 'sqrt', '/', 7, 8, 9, '*', 4, 5, 6, '+', 1, 2, 3, '-', 0, '=']

        self.ans_label = Label(self.frame, font=self.def_font)
        self.ans_label.grid(row=0, column=0, columnspan=4)
        self.frame.grid_rowconfigure(0, weight=1)
        for symb in self.symbs:
            self.create_button(symb, 1+self.symbs.index(symb)//4, self.symbs.index(symb)%4)

    def create_button(self, name, i, j):
        self.symb_button = Button(self.frame, font=self.def_font, text=name, width=3, 
                                  command=lambda name=name: self.operation(name))
        self.frame.grid_rowconfigure(i, weight=1)
        self.frame.grid_columnconfigure(j, weight=1)
        self.symb_button.grid(row=i, column=j, sticky='nsew')
        if name == '=':
            self.symb_button.grid(columnspan=3)

    def operation(self, name):
        if name == '+' and self.equation[-1] not in self.operators:
            self.equation += '+'
            self.ans_label.configure(text=self.equation)
        elif name == '-' and self.equation[-1] not in self.operators:
            self.equation += '-'
            self.ans_label.configure(text=self.equation)
        elif name == '*' and self.equation[-1] not in self.operators:
            self.equation += '*'
            self.ans_label.configure(text=self.equation)
        elif name == '/' and self.equation[-1] not in self.operators:
            self.equation += '/'
            self.ans_label.configure(text=self.equation)
        elif name == '^' and self.equation[-1] not in self.operators:
            self.equation += '**'
            self.ans_label.configure(text=self.equation)
        elif name == 'sqrt' and self.equation[-1] not in self.operators:
            self.equation += '**(1/2)'
            self.ans_label.configure(text=self.equation)
        elif name == 'C':
            self.equation = ''
            self.ans_label.configure(text=self.equation)
        elif name == '=' and self.equation[-1] not in self.operators:
            self.equation = str(eval(self.equation))
            self.ans_label.configure(text=self.equation)
        
        for num in range(10):
            if num == name:
                self.equation += str(name)
                self.ans_label.configure(text=self.equation)
        
if __name__ == '__main__':
    top = Tk()
    calculator = CalculatorGui(top)
    top.mainloop()