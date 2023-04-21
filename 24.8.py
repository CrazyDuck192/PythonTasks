from tkinter import *
import tkinter.messagebox as mb

class SegmentError(Exception):

    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return 'Початок відрізку повинен бути строго меншим за кінець'

class Vector:

    def __init__(self):
        self.top = Tk()
        self.font = ('Bahnschrift Light', 18)
        self.main_window()
        
    def main_window(self):
        self.n_label = Label(self.top, font=self.font, text='Довжина вектора:')
        self.n_label.grid(row=0, column=0, pady=3, sticky='e')
        self.n_entry = Entry(self.top, font=self.font)
        self.n_entry.grid(row=0, column=1, sticky='w')

        self.a_label = Label(self.top, font=self.font, text='Початок відрізку:')
        self.a_label.grid(row=1, column=0, sticky='e')
        self.a_entry = Entry(self.top, font=self.font)
        self.a_entry.grid(row=1, column=1, sticky='w')
        
        self.b_label = Label(self.top, font=self.font, text='Кінець відрізку:')
        self.b_label.grid(row=2, column=0, pady=3, sticky='e')
        self.b_entry = Entry(self.top, font=self.font)
        self.b_entry.grid(row=2, column=1, sticky='w')

        self.enter_button = Button(self.top, font=self.font, text='Підтвердити', width=15, command=self.enter_data)
        self.enter_button.grid(row=3, column=0, columnspan=2, pady=5)

    def enter_data(self):
        try:
            self.n = int(self.n_entry.get())
            self.a = int(self.a_entry.get())
            self.b = int(self.b_entry.get())
            if self.a >= self.b:
                raise SegmentError
        except ValueError:
            mb.showwarning('Увага!', 'Всі поля повинні бути заповнені та містити лише цілі числа')
        except SegmentError as e:
            mb.showwarning('Увага!', e)
        else:
            self.vector_top = Toplevel()
            self.vector_window()

    def vector_window(self):
        self.coords = []
        self.correct_coords = []
        self.v_label = Label(self.vector_top, font=self.font, text='Координата вектора:')
        self.v_label.grid(row=0, column=0, pady=5)
        self.v_entry = Entry(self.vector_top, font=self.font, width=5)
        self.v_entry.grid(row=0, column=1)
        self.v_entry.bind('<Return>', self.accept)

    def accept(self, event):
        try:
            coord = int(self.v_entry.get())
        except ValueError:
            mb.showwarning('Увага!', 'Поле має бути заповнено та містити ціле число')
        else:
            self.coords.append(coord)
            if self.a <= coord <= self.b:
                self.correct_coords.append(coord)
            self.v_entry.delete(0, END)
            if len(self.coords) == self.n:
                self.vector_top.destroy()
                self.create_vectors()

    def create_vectors(self):
        self.coords_label = Label(self.top, font=self.font, text='Координати вектора')
        self.coords_label.grid(row=4, column=0, pady=5, padx=3)
        self.coords_listbox = Listbox(self.top, font=self.font, justify='center', width=10, height=5)
        self.coords_listbox.grid(row=5, column=0)
        index = 1
        for coord in self.coords:
            self.coords_listbox.insert(END, f'x{index} = {coord}')
            index += 1
        
        self.correct_coords_label = Label(self.top, font=self.font, text='Координати на відрізку')
        self.correct_coords_label.grid(row=4, column=1, pady=5, padx=3)
        self.correct_coords_listbox = Listbox(self.top, font=self.font, justify='center', width=10, height=5)
        self.correct_coords_listbox.grid(row=5, column=1)
        index = 1
        for coord in self.correct_coords:
            self.correct_coords_listbox.insert(END, f'x{index} = {coord}')
            index += 1

    
if __name__ == '__main__':
    w = Vector()
    mainloop()