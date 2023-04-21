from random import choice
from time import time
import tkinter as tk

class TypingError(Exception):

    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return 'Неправильно набрано слово!'
    
class TimeError(Exception):

    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return 'Вичерпано ліміт часу!'

class TypingTutor:

    def __init__(self, file, words_number, type_time):
        self.filename = file
        self.data = []
        self.points = 0
        self.words_number = words_number
        self.type_time = type_time
        self.words_list = self.prepare_words()

    def prepare_words(self):
        with open(self.filename) as f:
            lines = f.readlines()
            words = set()
            words_list = []
            for word in lines:
                if len(word.strip()) > 3:
                    words.add(word.strip())
            length = 4
            words = list(words)
            while len(words_list) < self.words_number:
                count = 0
                while count != 2:
                    word = choice(words)
                    words.remove(word)
                    if len(word) == length:
                        words_list.append(word)
                        count += 1
                    if all([len(x) < length for x in words]):
                        length -= 1
                    elif all([len(x) != length for x in words]):
                        length += 1
                length += 1
        print(words_list)
        return words_list
                    
    def get_protocol(self):
        print(f'Набрано балів: {self.points}/{self.words_number}')
        print('Інформація: ')
        for word_data in self.data:
            print(word_data)

class TypingTutorGUI(TypingTutor):

    def __init__(self, file, words_number, type_time):
        TypingTutor.__init__(self, file, words_number, type_time)
        self.top = tk.Tk()
        self.def_font = ('Bahnschrift Light', 18)
        self.top.geometry('350x550')
        self.i = 0
        self.is_start = False
        self.create_widgets()
        self.typing_entry.focus_set()
        self.typing_entry.grab_set()
        self.typing_entry.bind('<Key>', self.start_tutor)      

    def create_widgets(self):
        self.word_label = tk.Label(self.top, font=self.def_font)
        self.word_label.pack(pady=15)
        self.word_label.config(text=self.words_list[self.i])
        self.typing_entry = tk.Entry(self.top, font=self.def_font)
        self.typing_entry.pack()
        self.words_listbox = tk.Listbox(self.top, font=self.def_font)
        self.words_listbox.pack(pady=15)
        self.points_label = tk.Label(self.top, font=self.def_font)
        self.points_label.pack(pady=10)
        self.restart_button = tk.Button(self.top, font=self.def_font, text='Restart', command=self.restart_tutor, width=20, relief='solid')

    def train(self):     
        self.word_label.config(text=self.words_list[self.i])
        self.start = time()
        
    def check_word(self, event):
        try:
            self.end = time()
            word = self.typing_entry.get()
            self.typing_entry.delete(0, tk.END)
            if word != self.words_list[self.i]:
                raise TypingError
            elif (self.end - self.start) > self.type_time:
                raise TimeError
        except TypingError as e:
            if self.points > 0:
                self.points -= 1
            string = f'[-1] {self.words_list[self.i]}'
            self.points_label.config(text=e)
        except TimeError as e:
            string = f'[0] {self.words_list[self.i]}'
            self.points_label.config(text=e)
        else:
            self.points += 1
            string = f'[+1] {self.words_list[self.i]}'
            self.points_label.config(text='')
        print(self.i)
        self.i += 1
        self.words_listbox.insert(0, string)
        try:
            self.train()
        except IndexError:
            self.typing_entry.config(state='disabled')
            self.points_label.config(text=f'Your points: {self.points}/{len(self.words_list)}')
            self.typing_entry.unbind('<Return>')
            self.typing_entry.grab_release()
            self.restart_button.pack()

    def start_tutor(self, event):
        self.typing_entry.bind('<Return>', self.check_word) 
        self.train()
        self.typing_entry.unbind('<Key>')

    def restart_tutor(self):
        self.top.destroy()
        TypingTutorGUI(self.filename, self.words_number, self.type_time)


if __name__ == '__main__':
    filename = 'hw/tutor_words.txt'
    tutor = TypingTutorGUI(filename, 10, 4)
    tk.mainloop()
        