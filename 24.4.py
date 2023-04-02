from tkinter import *

def sign_changes(nums=[], changes=0):
    num = float(number_entry.get())
    number_entry.delete(0, END)
    if num == 0:
        for i in range(len(nums)-1):
            if (nums[i] > 0 and nums[i+1] < 0) or (nums[i] < 0 and nums[i+1] > 0):
                changes += 1
        ans = changes
        while nums:
            nums.pop()
        changes = 0
        return ans
    else:
        nums.append(num)

def execution(ev=None):
    ans = sign_changes()
    if ans != None:
        ans_label.configure(text=f'Number of sign changes: {ans}')
        ans_label.pack()

top = Tk()

# Input number
number_frame = Frame(top)
number_frame.pack()
number_label = Label(number_frame, font=('arial', 16), text='Input number: ').pack(side=LEFT)
number_entry = Entry(number_frame, font=('arial', 16))
number_entry.pack()

# Button
accept_button = Button(top, font=('arial', 16), text='Accept', command=execution)
accept_button.pack()
top.bind('<Return>', execution)

# Answer
ans_label = Label(top, font=('arial', 16))

top.mainloop()