from tkinter import *

def is_palindrome(s):
    if s == s[::-1]:
        return 'YES'
    else:
        return 'NO'
    
def check():
    s = string_entry.get()
    ans = is_palindrome(s)
    ans_label.configure(text=f'Is palindrome: {ans}')
    
top = Tk()

# String
string_frame = Frame(top)
string_frame.pack()
Label(string_frame, font=('arial', 16), text='Input string: ').pack(side=LEFT)
string_entry = Entry(string_frame, font=('arial', 16))
string_entry.pack()

# Answer
ans_label = Label(top, font=('arial', 16), text='Is palindrome: ')
ans_label.pack()

# Button
Button(top, font=('arial', 16), text='Check string', command=check).pack()

top.mainloop()