from task_24_22 import *
from tkinter import *
from tkinter.font import Font
import json

class ScholarshipGUI:

    def __init__(self, frame, n_subjects:int, filename):
        self.frame = frame
        self.frame.option_add('*Font', '"Bahnschrift Light" 18')
        self.subjects = n_subjects
        self.file = filename

        self.main_window()

    def main_window(self):
        Label(self.frame, text='Студенти').grid(row=0, column=0)
        self.st_list = Listbox(self.frame)
        self.st_list.grid(row=1, column=0)

        Label(self.frame, text='Стипендія').grid(row=0, column=1)
        self.ss_list = Listbox(self.frame)
        self.ss_list.grid(row=1, column=1)
        self.ss_list.configure(width=11)
        self.update_list()

        self.st_button = Button(self.frame, text='Додати студента', command=self.input_student)
        self.st_button.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
        
        self.ss_button = Button(self.frame, text='Нарахувати стипендію', command=self.input_scholarship)
        self.ss_button.grid(row=3, column=0, padx=5, columnspan=2)

    def input_student(self):
        student_frame = Toplevel(self.frame)
        student_frame.title('Інформація про студента')
        new_student = Student(self.file)
        subjects_list = []
        marks_list = []
        student_data = {}

        Label(student_frame, text='Прізвище:').grid(row=0, column=0, padx=5, sticky='E')
        surname_entry = Entry(student_frame)
        surname_entry.grid(row=0, column=1, padx=5)

        Label(student_frame, text="Ім'я:").grid(row=1, column=0, padx=5, sticky='E')
        name_entry = Entry(student_frame)
        name_entry.grid(row=1, column=1, padx=5)

        Label(student_frame, text='Рік народження:').grid(row=2, column=0, padx=5, sticky='E')
        byear_entry = Entry(student_frame)
        byear_entry.grid(row=2, column=1, padx=5)

        Label(student_frame, text='Курс:').grid(row=3, column=0, padx=5, sticky='E')
        course_entry = Entry(student_frame)
        course_entry.grid(row=3, column=1, padx=5)

        for i in range(1, self.subjects+1):
            Label(student_frame, text='Предмет:').grid(row=3+i, column=0, sticky='E')
            subject_entry = Entry(student_frame)
            subject_entry.grid(row=3+i, column=1)
            Label(student_frame, text='Оцінка:').grid(row=3+i, column=2)
            mark_entry = Entry(student_frame, width=5)
            mark_entry.grid(row=3+i, column=3)
            subjects_list.append(subject_entry)
            marks_list.append(mark_entry)

        def get_data():
            new_student.surname = surname_entry.get()
            new_student.name = name_entry.get()
            new_student.byear = int(byear_entry.get())
            new_student.course = int(course_entry.get())
            for s, m in zip(subjects_list, marks_list):
                    new_student.marks[s.get()] = int(m.get())
            attrs = [attr for attr in dir(new_student) if not callable(getattr(new_student, attr)) and not attr.startswith("__")]
            for attr in reversed(attrs):
                if attr != 'file':
                    student_data[attr] = new_student.__dict__[attr]
            new_student.save(student_data)
            for widget in student_frame.winfo_children():
                if isinstance(widget, Entry):
                    if widget not in subjects_list:
                        widget.delete(0, END)

            self.update_list()

        accept_button = Button(student_frame, text='Підтвердити', command=get_data)
        accept_button.grid(row=3+i+1, column=1)

    def input_scholarship(self):
        scholarship_frame = Toplevel(self.frame)
        scholarship_frame.title('Нарахування стипендії')

        Label(scholarship_frame, text='Студенти').grid(row=0, column=0, columnspan=2)
        students_list = Listbox(scholarship_frame)

        def fill_list():
            students_list.delete(0, END)
            with open('exercises/24_22.json') as f:
                data = json.load(f)
                for x in data:
                    if 'scholarship' not in x:
                        st = f"{x['surname']} {x['name']}"
                        students_list.insert(END, st)

        fill_list()
        students_list.grid(row=1, column=0, columnspan=2)
        Label(scholarship_frame, text='Стипендія:').grid(row=2, column=0, pady=5)
        scholarship_entry = Entry(scholarship_frame)
        scholarship_entry.grid(row=2, column=1, pady=5)

        def accrual():
            scholarship_value = int(scholarship_entry.get())
            selected_student = students_list.get(students_list.curselection()[0])
            with open('exercises/24_22.json', 'r+') as f:
                data = json.load(f)
                for x in data:
                    if x['surname'] == selected_student.split()[0] and x['name'] == selected_student.split()[1]:
                        x['scholarship'] = scholarship_value
                        break
                f.seek(0)
                json.dump(data, f, indent=4)
            fill_list()
            self.update_list()

        accrual_button = Button(scholarship_frame, text='Нарахувати', command=accrual)
        accrual_button.grid(row=3, column=0, pady=5, columnspan=2)

    def update_list(self):
        list_width = 15
        self.st_list.delete(0, END)
        self.ss_list.delete(0, END)
        with open("exercises/24_22.json") as f:
            data = json.load(f)
            for x in data:
                st = f" {x['surname']} {x['name']}"
                if 'scholarship' in x:
                    self.ss_list.insert(END, ' Нараховано')
                else:
                    self.ss_list.insert(END, '')
                if len(st) > list_width:
                    list_width = len(st)
                self.st_list.insert(END, st)
        self.st_list.configure(width=list_width)

if __name__ == '__main__':
    filename = 'exercises/24_22.json'
    top = Tk()
    gui = ScholarshipGUI(top, 1, filename)
    mainloop()