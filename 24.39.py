"""Скласти програму з графічним інтерфейсом для
розв’язання задачі.
Задані n точок площини. Провести коло мінімального радіусу
так, щоб усі точки лежали всередині кола.
Завдання точок здійснити у графічному режимі на полотні
(натисненням у потрібній позиції лівої клавіші миші).
Побудоване коло також показати у графічному режимі."""
from tkinter import *
from math import sqrt, pi

top = Tk()
canvas = Canvas(top, width=400, height=400)
canvas.pack()
points_list = []
def set_point(event):
    global points_list
    x1 = event.x
    y1 = event.y
    points_list.append((x1, y1))
    canvas.create_oval(x1-5, y1-5, x1+5, y1+5, fill='black')

def calculate(event):
    global points_list
    global canvas
    r0 = 0
    area_dict = {}
    for a in range(len(points_list)-1):
        for b in range(a, len(points_list)):
            x0 = (points_list[a][0] + points_list[b][0])/2
            y0 = (points_list[a][1] + points_list[b][1])/2
            while not all([sqrt((p[0] - x0)**2 + (p[1] - y0)**2)<=r0/2 for p in points_list]):
                r0 += 1
            area_dict[pi*r0**2] = (x0, y0, r0)
            r0 = 0
    params = area_dict[min(area_dict.keys())]
    x1 = params[0] - params[2]/2
    y1 = params[1] - params[2]/2
    x2 = params[0] + params[2]/2
    y2 = params[1] + params[2]/2
    canvas.create_oval(x1, y1, x2, y2)

canvas.bind('<Button-1>', set_point)
canvas.bind('<Button-3>', calculate)
top.mainloop()

