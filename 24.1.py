from tkinter import *

def func(x, eps):    
    y = 1
    y_0 = 1
    n = 2
    while abs(y_0) >= eps:
        y_0 = (-1)**(n+1) * n * x**(n-1)
        y += y_0
        print(y)
        n += 1

    return y

def calc():
    x = float(x_entry.get())
    eps = float(eps_entry.get())
    assert abs(x) < 1, result_label.configure(text='Warning! |x| < 1')
    assert eps > 0, result_label.configure(text='Warning! eps > 0')
    ans = func(x, eps)
    result_label.configure(text=f'Result: {ans}')
    
top = Tk()

# X
x_frame = Frame(top)
x_frame.pack()
Label(x_frame, font=('arial', 16), text='    X: ').pack(side=LEFT)
x_entry = Entry(x_frame, font=('arial', 16))
x_entry.pack()

# Eps
eps_frame = Frame(top)
eps_frame.pack()
Label(eps_frame, font=('arial', 16), text='Eps: ').pack(side=LEFT)
eps_entry = Entry(eps_frame, font=('arial', 16))
eps_entry.pack()

# Result
result_frame = Frame(top)
result_frame.pack()
result_label = Label(result_frame, font=('arial', 16), text='Result: ')
result_label.pack(side=LEFT)

# Button
calc_button = Button(top, font=('arial', 16), text="Calculate", command=calc)
calc_button.pack()

top.mainloop()