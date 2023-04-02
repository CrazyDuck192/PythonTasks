from tkinter import *

def max_length(s):
    max_l = 0
    index = 0
    start = 0
    end = 0
    for letter_0 in s:
        l = 0
        for letter_1 in s[index:]:
            if letter_0 != letter_1:
                break
            l += 1
        if l > max_l:
            start = index
            end = start + l - 1
            max_l = l
        index += 1
    return start, end

def execution():
    start, end = max_length(string_entry.get())
    ans_label_left.configure(text=f'{string_entry.get()[:start]}')
    ans_label_left.pack(side='left')
    ans_label_center.configure(text=f'{string_entry.get()[start:end+1]}')
    ans_label_center.pack(side='left')
    ans_label_right.configure(text=f'{string_entry.get()[end+1:]}')
    ans_label_right.pack(side='left')

top = Tk()

# String
string_frame = Frame(top)
string_frame.pack()
Label(string_frame, font=('arial', 16), text='Input string: ').pack(side=LEFT)
string_entry = Entry(string_frame, font=('arial', 16))
string_entry.pack()

# Button
check_button = Button(top, font=('arial', 16), text='Accept', command=execution)
check_button.pack()

# Answer
ans_frame = Frame(top)
ans_frame.pack()
ans_label_left = Label(ans_frame, font=('arial', 16))
ans_label_center = Label(ans_frame, font=('arial', 16), background='orange')
ans_label_right = Label(ans_frame, font=('arial', 16))

top.mainloop()