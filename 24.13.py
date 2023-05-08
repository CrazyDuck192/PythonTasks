from tkinter import *

class BooksGUI:

    def __init__(self, frame, filename):
        self.filename = filename
        self.frame = frame
        self.def_font = ('Bahnschrift Light', 16)
        self.create_checkbuttons()
        self.books_lb = Listbox(self.frame, font=self.def_font, width=0)
        
    def create_checkbuttons(self):
        Label(self.frame, font=self.def_font, text='Choose parameters').grid(row=0, column=0, columnspan=3)
        self.author_var = BooleanVar()
        self.author_cb = Checkbutton(self.frame, variable=self.author_var, font=self.def_font, text='Author')
        self.author_cb.grid(row=1, column=0)
        self.title_var = BooleanVar()
        self.title_cb = Checkbutton(self.frame, variable=self.title_var, font=self.def_font, text='Title')
        self.title_cb.grid(row=1, column=1)
        self.year_var = BooleanVar()
        self.year_cb = Checkbutton(self.frame, variable=self.year_var, font=self.def_font, text='Year')
        self.year_cb.grid(row=1, column=2)
        Button(self.frame, font=self.def_font, text='Accept', command=self.accept_params).grid(row=2, column=1)

    def accept_params(self):
        if self.author_var.get() or self.title_var.get() or self.year_var.get():
            self.params_window = Toplevel(self.frame)
            self.r = 0

            if self.author_var.get():
                Label(self.params_window, font=self.def_font, text='Author: ').grid(row=self.r, column=0)
                self.author_entry = Entry(self.params_window, font=self.def_font)
                self.author_entry.grid(row=self.r, column=1)
                self.r += 1

            if self.title_var.get():
                Label(self.params_window, font=self.def_font, text='Title: ').grid(row=self.r, column=0)
                self.title_entry = Entry(self.params_window, font=self.def_font)
                self.title_entry.grid(row=self.r, column=1)
                self.r += 1

            if self.year_var.get():
                Label(self.params_window, font=self.def_font, text='From: ').grid(row=self.r, column=0)
                self.year_from_entry = Entry(self.params_window, font=self.def_font)
                self.year_from_entry.grid(row=self.r, column=1)
                Label(self.params_window, font=self.def_font, text='To: ').grid(row=self.r+1, column=0)
                self.year_to_entry = Entry(self.params_window, font=self.def_font)
                self.year_to_entry.grid(row=self.r+1, column=1)
                self.r += 2

            Button(self.params_window, font=self.def_font, text='Accept', command=self.create_books_list).grid(row=self.r, column=0, columnspan=2)

    def create_books_list(self):
        self.books_lb.delete(0, END)
        self.params_dict = {}
        self.books_list = []
        try:
            if self.author_var.get():
                self.params_dict['author_data'] = self.author_entry.get()
                if self.params_dict['author_data'] == '':
                    raise ValueError               
            if self.title_var.get():
                self.params_dict['title_data'] = self.title_entry.get()
                if self.params_dict['title_data'] == '':
                    raise ValueError
            if self.year_var.get():
                self.params_dict['year_data'] = (int(self.year_from_entry.get()),
                                                 int(self.year_to_entry.get()))
            self.params_window.destroy()
            with open(self.filename) as f:
                lines = f.readlines()
                for line in lines:
                    self.is_inlist = True
                    for key in self.params_dict.keys():
                        if key == 'year_data':
                            if int(line.split()[-1].rstrip('\n')) not in range(self.params_dict[key][0], self.params_dict[key][1]+1):
                                self.is_inlist = False
                        else:
                            if self.params_dict[key] not in line:
                                self.is_inlist = False
                    if self.is_inlist:
                        self.books_list.append(line)
            self.length = max([len(line) for line in self.books_list])
            for book in self.books_list:
                self.books_lb.insert(END, book)
            self.books_lb.configure(width=self.length)
            self.books_lb.grid(row=3, column=0, columnspan=3)
        except ValueError:
            pass       

if __name__ == '__main__':
    filename = 'exercises/24.13.txt'
    frame = Tk()
    top = BooksGUI(frame, filename)
    mainloop()