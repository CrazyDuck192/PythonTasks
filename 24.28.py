"""Скласти програму з графічним інтерфейсом для 
проведення тестування. Питання можуть підтримувати вибір 
одного або декількох варіантів з багатьох альтернатив. Питання 
та відповіді зберігаються у файлі з позначенням правильного 
варіанту (ів) відповіді. Програма повинна читати питання, 
виводити їх на екран, отримувати та зберігати відповіді. Після 
завершення тестування – аналізувати відповіді та повідомляти 
кількість правильних відповідей. Забезпечити контроль часу 
проходження тесту, вважаючи, що максимальний час також 
зберігається у файлі. Забезпечити навчальний режим 
тестування, надавши можливість після проходження тесту 
подивитись правильні відповіді на кожне питання а також надані 
відповіді."""

from tkinter import *
import json

class QuizGui:

    def __init__(self, gui, questions):
        self.frame = gui
        self.count = 0
        self.count_correct = 0
        self.def_font = ('arial', 16)
        self.var = IntVar()

        self.questions = questions['Questions']
        self.options = questions['Options']
        self.answers = questions['Answers']
        self.n = len(self.questions)

        Button(self.frame, font=self.def_font, text='Start', command=self.show_question).pack()
        Button(self.frame, font=self.def_font, text='Close', command=self.close).pack()

    def show_question(self):
        if self.count > 0:
            if self.var.get() == self.options[self.count-1][self.answers[self.count-1]]:
                self.count_correct += 1
        if self.count == self.n:
            self.create_results()
        else:
            self.create_question(self.questions[self.count], 
                                    self.options[self.count])
                
            Button(self.frame, font=self.def_font, text='Next', command=self.show_question).pack()
        self.count += 1

    def create_question(self, question, option):
        for widget in self.frame.winfo_children():
            widget.destroy()
        Label(self.frame, font=self.def_font, text=f'№{self.count+1}').pack()
        Label(self.frame, font=self.def_font, text=question).pack()
        for i in option:
            radio = Radiobutton(self.frame, font=self.def_font, text=i, variable=self.var, value=i)
            radio.deselect()
            radio.pack()

    def create_results(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        Label(self.frame, font=self.def_font, text=f'Results: {self.count_correct}/{self.n}').grid(row=0, column=0)
        for n, i in enumerate(zip(self.questions, self.answers)):
            Label(self.frame, font=self.def_font, text=f'{n+1}) {i[0]}{self.options[n][i[1]]}').grid(row=n+1, column=0)

    def close(self):
        self.frame.quit()

if __name__ == '__main__':

    filename = 'exercises/quizes.json'
    questions = json.load(open(filename))
    print(questions)

    gui = Tk()
    QuizGui(gui, questions)
    gui.mainloop()
