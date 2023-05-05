from random import randint, choice
from tkinter import *
import pygame
import pygame.mixer as pgm
import tkinter.messagebox as mb

class Tetris:

    def __init__(self, width, height, rows, cols):
        self.top = Tk()
        self.top.title('Tetris')
        # pygame.init()
        # pgm.music.load('exercises/sounds/tetris.mp3')
        # pgm.music.set_volume(0.1)
        self.top.resizable(False, False)
        self.canvas = Canvas(self.top, width=width+300, height=height)
        self.width = width
        self.height = height
        self.canvas.pack()
        self.rows = rows
        self.cols = cols
        self.cellsize = width//cols
        self.grid_list = []
        self.key_pressed = []
        self.rects_list = [[None for _ in range(self.cols-2)] for _ in range(self.rows-2)]
        self.colors = ['yellow', 'red', 'green', 'orange', 'blue', 'violet', 'cyan']
        self.points = 0

        # Управління
        self.top.bind('<KeyPress>', self.move_shape)
        self.top.bind('<KeyRelease>', self.key_released)

        # Реалізація гри
        self.create_grid()
        self.create_infomenu()
        self.shape = self.create_shape(randint(0, 6), choice(self.colors))
        self.next_shape = self.create_next(randint(0, 6), choice([color for color in self.colors if color != self.this_color]))
        # pgm.music.play(-1)
        self.moving()

    def create_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.canvas.create_rectangle(self.cellsize*col, self.cellsize*row, 
                                             self.cellsize*(col+1), self.cellsize*(row+1),
                                             fill='black')
                
        for col in range(self.cols):
            self.canvas.create_rectangle(self.cellsize*col, 0, self.cellsize*(col+1), 
                                         self.cellsize, fill='grey')
        for row in range(self.rows):
            self.canvas.create_rectangle(0, self.cellsize*row, self.cellsize, 
                                         self.cellsize*(row+1), fill='grey')
        for row in range(self.rows):
            self.canvas.create_rectangle(self.cellsize*(self.cols-1), self.cellsize*row, 
                                         self.cellsize*self.cols, self.cellsize*(row+1), fill='grey')
        for col in range(self.cols):
            self.canvas.create_rectangle(self.cellsize*col, self.cellsize*(self.rows-1), 
                                         self.cellsize*(col+1), self.cellsize*self.rows, fill='grey')

    def create_shape(self, shape_id, color):
        self.this_color = color
        self.shape_id = shape_id
        lst = []
        dx = self.cols//2
        ds = self.cellsize
        self.coords_list = [((dx*ds, 0, (dx+1)*ds, ds), ((dx+1)*ds, 0, (dx+2)*ds, ds),
                         (dx*ds, ds, (dx+1)*ds, ds*2), ((dx+1)*ds, ds, (dx+2)*ds, ds*2)),
                        ((dx*ds, 0, (dx+1)*ds, ds), ((dx-1)*ds, ds, dx*ds, ds*2),
                         (dx*ds, ds, (dx+1)*ds, ds*2), ((dx+1)*ds, ds, (dx+2)*ds, ds*2)),
                        ((ds*dx, 0, (dx+1)*ds, ds), ((dx-1)*ds, ds, dx*ds, ds*2),
                         (dx*ds, ds, (dx+1)*ds, ds*2), ((dx+1)*ds, 0, (dx+2)*ds, ds)),
                        ((dx*ds, 0, (dx+1)*ds, ds), ((dx-1)*ds, 0, dx*ds, ds),
                         (dx*ds, ds, (dx+1)*ds, ds*2), ((dx+1)*ds, ds, (dx+2)*ds, ds*2)),
                        ((dx*ds, 0, (dx+1)*ds, ds), (dx*ds, ds, (dx+1)*ds, ds*2),
                         ((dx+1)*ds, ds, (dx+2)*ds, ds*2), ((dx+2)*ds, ds, (dx+3)*ds, ds*2)),
                        ((dx*ds, 0, (dx+1)*ds, ds), ((dx-2)*ds, ds, (dx-1)*ds, ds*2),
                         ((dx-1)*ds, ds, dx*ds, ds*2), (dx*ds, ds, (dx+1)*ds, ds*2)),
                        (((dx-1)*ds, 0, dx*ds, ds), (dx*ds, 0, (dx+1)*ds, ds),
                         ((dx+1)*ds, 0, (dx+2)*ds, ds), ((dx+2)*ds, 0, (dx+3)*ds, ds))]
        
        rects = self.coords_list[shape_id]
        for rect in rects:
            r = self.canvas.create_rectangle(rect[0], rect[1], rect[2], rect[3], fill=color)
            lst.append(r)
        
        return lst
    
    def create_infomenu(self):
        Label(self.canvas, text='Next shape', font=('Arial', 32)).place(
            x=self.cellsize*(self.cols+1), y=self.cellsize)
        Label(self.canvas, text='Score', font=('Arial', 32)).place(
            x=self.cellsize*(self.cols+2.5), y=self.cellsize*6)
        self.score_label = Label(self.canvas, text=self.points, font=('Arial', 32), width=8)
        self.score_label.place(x=self.cellsize*(self.cols+1.2), y=self.cellsize*7.5)
    
    def create_next(self, shape_id, color):
        lst = []
        self.next_id = shape_id
        self.next_color = color

        rects = self.coords_list[shape_id]
        dx = self.cellsize*(self.cols+7)//2
        dy = self.cellsize*3
        for rect in rects:
            r = self.canvas.create_rectangle(rect[0]+dx, rect[1]+dy, rect[2]+dx, rect[3]+dy, fill=color)
            lst.append(r)
        
        return lst
        
    def moving(self):
        self.is_moving()

        for r in self.shape:
            self.canvas.move(r, 0, self.cellsize)


    def move_shape(self, event):
        if event.keysym == 'Right' and self.check_collision(self.cellsize, 0):
            if max([self.canvas.coords(r0)[2] for r0 in self.shape]) < self.width-self.cellsize:
                for r in self.shape:
                    self.canvas.move(r, self.cellsize, 0)  
                    
        elif event.keysym == 'Left' and self.check_collision(-self.cellsize, 0):
            if all([self.canvas.coords(r0)[0] > 0+self.cellsize for r0 in self.shape]):
                for r in self.shape:
                    self.canvas.move(r, -self.cellsize, 0)

        elif event.keysym == 'Down':
            self.canvas.after_cancel(self.move)
            self.is_moving()
            for r in self.shape:
                self.canvas.move(r, 0, self.cellsize)


        elif event.keysym == 'Up' and 'Up' not in self.key_pressed:
            self.key_pressed.append('Up')
            self.turn_shape()

    def turn_shape(self):
        center = self.shape[2]
        r_color = self.canvas.itemcget(center, 'fill')
        coords = []

        if self.shape_id in range(1, 7):
            for rect in [r for r in self.shape if r != center]:
                if self.canvas.coords(rect)[1] == self.canvas.coords(center)[1]:
                    dv = self.canvas.coords(rect)[0] - self.canvas.coords(center)[0]
                    x = self.canvas.coords(rect)[0] - dv
                    y = self.canvas.coords(rect)[1] + dv
                elif self.canvas.coords(rect)[0] == self.canvas.coords(center)[0]:
                    dv = self.canvas.coords(center)[1] - self.canvas.coords(rect)[1]
                    x = self.canvas.coords(rect)[0] + dv
                    y = self.canvas.coords(rect)[1] + dv
                elif self.canvas.coords(rect)[1] > self.canvas.coords(center)[1]:
                    dv = self.canvas.coords(rect)[0] - self.canvas.coords(center)[0]
                    if dv < 0:
                        x = self.canvas.coords(rect)[0]
                        y = self.canvas.coords(rect)[1] + 2*dv
                    else:
                        x = self.canvas.coords(rect)[0] - 2*dv
                        y = self.canvas.coords(rect)[1]
                else:
                    dv = self.canvas.coords(rect)[0] - self.canvas.coords(center)[0]
                    if dv < 0:
                        x = self.canvas.coords(rect)[0] - 2*dv
                        y = self.canvas.coords(rect)[1]
                    else:
                        x = self.canvas.coords(rect)[0] 
                        y = self.canvas.coords(rect)[1] + 2*dv
                coords.append((x, y))

        elif self.shape_id == 0:
            for rect in [r for r in self.shape if r != center]:
                x = self.canvas.coords(rect)[0]
                y = self.canvas.coords(rect)[1]
                coords.append((x, y))
            
        for row in self.rects_list:
            for rect in row:
                for c in coords:
                    try:
                        if self.canvas.coords(rect)[0] == c[0] and self.canvas.coords(rect)[1] == c[1]:
                            return
                    except TclError:
                        pass
        
        coords.insert(2, (self.canvas.coords(center)[0], self.canvas.coords(center)[1]))
        for rect in self.shape:
            self.canvas.delete(rect)
        self.shape = []
        pushx, pushx0, pushy, pushy0 = 0, 0, 0, 0
        for c in coords:
            r = self.canvas.create_rectangle(c[0], c[1], c[0]+self.cellsize, c[1]+self.cellsize, fill=r_color)
            if c[0] < self.cellsize:
                pushx0 = self.cellsize - c[0]
            elif c[0] > self.cellsize*(self.cols-2):
                pushx0 = self.cellsize*(self.cols-2) - c[0]
            if abs(pushx0) > abs(pushx):
                pushx = pushx0
            
            if c[1] < self.cellsize:
                pushy0 = self.cellsize - c[1]
            elif c[1] > self.cellsize*(self.rows-2):
                pushy0 = self.cellsize*(self.rows-2) - c[1]
            if abs(pushy0) > abs(pushy):
                pushy = pushy0

            self.shape.append(r)
        for r in self.shape:
            self.canvas.move(r, pushx, pushy)

    def check_collision(self, x, y):
        lst = []
        for r in self.shape:
            x1, y1, x2, y2 = self.canvas.coords(r)
            lst.append((x1, y1, x2, y2))

        for row in self.rects_list:
            for rect in row:
                try:
                    x1, y1, x2, y2 = self.canvas.coords(rect)
                    for r in lst:
                        if r[0] + x == x1 and r[1] + y == y1:
                            return False
                except TclError:
                    pass

        return True

    def is_moving(self):
        if not all([self.canvas.coords(r)[3] < self.height-self.cellsize for r in self.shape]) or\
        not self.check_collision(0, self.cellsize):
            for r in self.shape:
                i = self.canvas.coords(r)[0]//self.cellsize
                j = self.canvas.coords(r)[1]//self.cellsize
                self.rects_list[int(j)-1][int(i)-1] = r
            
            self.is_row()
            self.shape = self.create_shape(self.next_id, self.next_color)
            for r in self.next_shape:
                self.canvas.delete(r)
            self.next_shape = self.create_next(randint(0, 6), 
                                               choice([color for color in self.colors if color != self.this_color]))
            
        if not self.is_loss():
            self.move = self.canvas.after(750, self.moving)


    def is_row(self):
        multiply = 0
        points = 0
        for row in self.rects_list:
            if None not in row:
                points += 10
                multiply += 1
                index = self.rects_list.index(row)
                self.rects_list.remove(row)
                for rect in row:
                    self.canvas.delete(rect)
                self.rects_list.insert(0, [None for _ in range(self.cols-2)])
                for row_new in self.rects_list[:index+1]:
                    for rect in row_new:
                        try:
                            self.canvas.move(rect, 0, self.cellsize)
                        except TclError:
                            pass
        self.points += points*multiply
        self.score_label.config(text=self.points)

    def is_loss(self):
        if not all(r == None for r in self.rects_list[0]):
            self.msg = mb.askyesno('Game over', 'Play again?')
            if self.msg:
                self.top.destroy()
                Tetris.__init__(self, 420, 770, 22, 12)
                return True
            else:
                exit()
        return False
    
    def key_released(self, event):
        if event.keysym in self.key_pressed:
            self.key_pressed.remove(event.keysym)

       
if __name__ == '__main__':
    game = Tetris(420, 770, 22, 12)
    mainloop()