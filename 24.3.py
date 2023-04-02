from tkinter import *

def diff_words(s):
    return set(s.split())

def make_list():
    string = diff_words(string_entry.get())
    words_list.delete(0, END)
    for word in string:
        words_list.insert(END, word)
    words_list.pack()

top = Tk()

# String
string_frame = Frame(top)
string_frame.pack()
Label(string_frame, font=('arial', 16), text='Input string: ').pack(side=LEFT)
string_entry = Entry(string_frame, font=('arial', 16))
string_entry.pack()

# Button
Button(top, font=('arial', 16), text='Accept', command=make_list).pack()

# Words list
words_list = Listbox(top, font=('arial', 16))

top.mainloop()
