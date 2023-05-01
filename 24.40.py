from tkinter import *
from time import strftime
from math import cos, sin, radians, pi

root = Tk()
root.title('Clock')
root.geometry('400x400')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root, width=390, height=390)
canvas.grid(padx=5, pady=5)

def track_time(hr, mi, se):
    canvas.create_oval(50, 50, 350, 350, fill='#c78665', outline='black', width=6)

    numbers = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]

    for i in range(len(numbers)):        
        canvas.create_text(200 - 120 * sin(((i+1)*2*pi)/12), 
                            200 - 120 * cos(((i+1)*2*pi)/12), text=numbers[i], 
                            font=('Arial',12, 'bold'), fill='white')

    for y in range(60):
        canvas.create_text(200 - 140 * sin(((y+1)*2*pi)/60), 
                            200 - 140 * cos(((y+1)*2*pi)/60), text='•', 
                            font=('Arial',12, 'bold'), fill ='#2853d4')

    for x in range(12):
        canvas.create_text(200 - 140 * sin(((x+1)*2*pi)/12), 
                            200 - 140 * cos(((x+1)*2*pi)/12), 
                            text='•', font=('Arial',25, 'bold'), fill ='#db341a')

    canvas.create_line(200, 200, 200 + 60*sin(radians(hr)), 
                    200 - 60*cos(radians(hr)), fill='#e6ab22', 
                    width=9, arrow= LAST)
    
    canvas.create_line(200, 200, 200 + 80*sin(radians(mi)), 
                    200 - 80*cos(radians(mi)), fill='#228ee6',
                        width=6, arrow= LAST)
    
    canvas.create_line(200, 200, 200 + 120*sin(radians(se)), 
                        200 - 120*cos(radians(se)), fill='red',
                        width=3,arrow= LAST)
    
    canvas.create_oval(190, 190, 210, 210, fill='black', width=2)

def some_time():
    h = int(strftime('%H'))
    m = int(strftime('%M'))
    s = int(strftime('%S'))

    hr = (h / 12) * 360
    mi = (m / 60) * 360
    se = (s / 60) * 360

    track_time(hr, mi, se)
    canvas.after(1000, some_time)

some_time()
mainloop()