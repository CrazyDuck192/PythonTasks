from tkinter import *
import tkinter.messagebox as mb

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
        self.n_entry.focus_set()
        self.n_entry.bind('<Return>', self.enter_data)

        self.enter_button = Button(self.top, font=self.font, text='Підтвердити', width=15, command=self.enter_data)
        self.enter_button.grid(row=1, column=0, columnspan=2, pady=5)

    def enter_data(self, event=None):
        try:
            self.n = int(self.n_entry.get())
        except ValueError:
            mb.showwarning('Увага!', 'Поле повинно бути заповнено та містити ціле число')
        else:
            self.vector_top = Toplevel()
            self.is_vector = 1
            self.vector_list1 = []
            self.vector_list2 = []
            self.vector_window()

    def vector_window(self):
        if self.is_vector == 1:
            self.v_label = Label(self.vector_top, font=self.font, text='Координата вектора 1:')
            self.v_label.grid(row=0, column=0, pady=5)
            self.v_entry = Entry(self.vector_top, font=self.font, width=5)
            self.v_entry.grid(row=0, column=1)
        else:
            self.v_label = Label(self.vector_top, font=self.font, text='Координата вектора 2:')
            self.v_label.grid(row=0, column=0, pady=5)
            self.v_entry = Entry(self.vector_top, font=self.font, width=5)
            self.v_entry.grid(row=0, column=1)
        self.v_entry.focus_set()
        self.v_entry.grab_set()
        self.v_entry.bind('<Return>', self.accept)

    def accept(self, event):
        try:
            coord = int(self.v_entry.get())
        except ValueError:
            mb.showwarning('Увага!', 'Поле має бути заповнено та містити ціле число')
        else:
            if self.is_vector == 1:
                self.vector_list1.append(coord)
                self.v_entry.delete(0, END)
                if len(self.vector_list1) == self.n:
                    self.is_vector = 2
                    self.vector_top.destroy()
                    self.vector_top = Toplevel(self.top)
                    self.vector_window()
            else:
                self.vector_list2.append(coord)
                self.v_entry.delete(0, END)
                if len(self.vector_list2) == self.n:
                    self.vector_top.destroy()
                    self.create_vectors()
                    self.scalar_product()

    def create_vectors(self):
        Label(self.top, font=self.font, text='Вектор 1').grid(row=2, column=0)
        self.vector1_listbox = Listbox(self.top, font=self.font, justify='center', width=10, height=5)
        self.vector1_listbox.grid(row=3, column=0)
        index = 1
        for coord in self.vector_list1:
            self.vector1_listbox.insert(END, f'x{index} = {coord}')
            index += 1

        Label(self.top, font=self.font, text='Вектор 2').grid(row=2, column=1)
        self.vector2_listbox = Listbox(self.top, font=self.font, justify='center', width=10, height=5)
        self.vector2_listbox.grid(row=3, column=1)
        index = 1
        for coord in self.vector_list2:
            self.vector2_listbox.insert(END, f'x{index} = {coord}')
            index += 1

    def scalar_product(self):
        p = 0
        for a, b in zip(self.vector_list1, self.vector_list2):
            p += a*b
        
        self.product_label = Label(self.top, font=self.font, text=f'Скалярний добуток: {p}')
        self.product_label.grid(row=4, column=0, columnspan=2, pady=5)

if __name__ == '__main__':
    v = Vector()
    mainloop()