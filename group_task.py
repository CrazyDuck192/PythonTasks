from tkinter import *
from tkinter import ttk

class FormConstructorGUI:

    def __init__(self, filename, form):
        self.top = form
        self.top.title('Form')
        self.def_font = ('Bahnschrift Light', 16)
        self.form_fields = {}
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                self.form_fields[line.split()[0]] = line.split()[1]
        self.show_form()

    def create_form(self):
        self.form_dict = {}
        for title in self.form_fields.keys():
            new_label = Label(self.top, font=self.def_font, text=title)
            if self.form_fields[title] == '{}':
                new_entry = Entry(self.top, font=self.def_font)
                self.form_dict[new_label] = new_entry
            else:
                value = StringVar()
                values_list = self.form_fields[title].rstrip(']').lstrip('[').split(',')
                new_cb = ttk.Combobox(self.top, value=value, values=values_list, state='readonly', font=self.def_font)
                self.form_dict[new_label] = new_cb

    def show_form(self):
        self.create_form()
        self.r = 0
        for k, v in self.form_dict.items():
            k.grid(row=self.r, column=0, pady=5, sticky='nsew')
            v.grid(row=self.r, column=1, pady=5, sticky='nsew')
            self.r += 1
        for i in range(len(self.form_dict)):
            self.top.grid_rowconfigure(i, weight=1)
            self.top.grid_columnconfigure(i, weight=1)
        self.create_buttons()
        self.fields_warning = Label(self.top, font=self.def_font, text='All fields must be filled in!')
        self.file_warning = Label(self.top, font=self.def_font, text='No forms in file')

    def create_buttons(self):
        cancel_button = Button(self.top, font=self.def_font, text='Cancel', command=self.delete_input)
        cancel_button.grid(row=self.r+1, column=0, pady=5, padx=10, sticky='nsew')
        accept_button = Button(self.top, font=self.def_font, text='Accept', command=self.accept_input)
        accept_button.grid(row=self.r+1, column=1, pady=5, padx=10, sticky='nsew')
        next_button = Button(self.top, font=self.def_font, text='Next', command=self.next_input)
        next_button.grid(row=self.r+1, column=2, pady=5, padx=10, sticky='nsew')

    def delete_input(self):
        for v in self.form_dict.values():
            if isinstance(v, Entry):
                v.delete(0, END)

    def next_input(self):
        self.fields_warning.grid_forget()
        self.file_warning.grid_forget()
        with open('exercises/form_data.txt', 'a') as f:
            data_list = []
            for v in self.form_dict.values():
                data = v.get()
                if data == '':
                    self.fields_warning.grid(row=self.r+2, column=1)
                    break
                if list(self.form_dict.values()).index(v) != len(self.form_dict)-1:
                    data_list.append(f'"{data}",')
                else:
                    data_list.append(f'"{data}"\n')
            if len(data_list) == len(self.form_dict):
                for i in data_list:
                    f.write(i)
                for v in self.form_dict.values():
                    v.delete(0, END)

    def accept_input(self):
        self.next_input()
        self.fields_warning.grid_forget()
        self.create_results_window()

    def create_results_window(self):
        self.results = Toplevel(self.top)
        self.lb = Listbox(self.results, font=self.def_font)
        try:
            with open('exercises/form_data.txt') as f:
                lines = f.readlines()
                if len(lines) > 0:
                    length = max(len(line) for line in lines)
                else:
                    self.file_warning.grid(row=self.r+2, column=1)
                    self.results.destroy()
                for line in lines:
                    self.lb.insert(END, line)
            self.lb.config(width=length)
            self.lb.grid(row=0, column=0, columnspan=2)
            Button(self.results, font=self.def_font, text='Delete', command=self.delete_selected).grid(row=1, column=0)
            Button(self.results, font=self.def_font, text='Finish', command=self.top.quit).grid(row=1, column=1)
        except UnboundLocalError:
            pass

    def delete_selected(self):
        selected_indices = self.lb.curselection()
        with open('exercises/form_data.txt', 'r+') as f:
            lines = f.readlines()
            for index in selected_indices:
                self.lb.delete(index)
                del lines[index]
            f.seek(0)
            f.writelines(lines)
            f.truncate()

if __name__ == '__main__':
    filename = 'exercises/group_task.txt'
    form = Tk()
    f = FormConstructorGUI(filename, form)
    mainloop()
