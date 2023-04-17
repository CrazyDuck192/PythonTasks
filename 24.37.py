from tkinter import *
from random import randint
from time import sleep
import tkinter.messagebox as mb

class HanoiGUI:

    def __init__(self):
        self.frame = Tk()
        self.def_font = ('Bahnschrift Light', 18)
        self.create_options()
        self.canvas = Canvas(self.frame, width=800, height=400)
        self.canvas.grid(row=1, column=0, columnspan=3)

        self.create_sticks()

    def create_sticks(self):
        self.stick1 = self.canvas.create_rectangle(180, 400, 200, 200, fill='black')
        self.stick1_list = []
        self.stick2 = self.canvas.create_rectangle(380, 400, 400, 200, fill='black')
        self.stick2_list = []
        self.stick3 = self.canvas.create_rectangle(580, 400, 600, 200, fill='black')
        self.stick3_list = []

    def create_disks(self):
        for stick in (self.stick1_list, self.stick2_list, self.stick3_list):
            for rect in stick:
                self.canvas.delete(rect)
            while stick:
                stick.pop()

        self.n = int(self.disks_entry.get())
        self.stick1_list = []
        self.height = 180//self.n
        dx = 50//self.n
        for i in range(self.n):
            disk = self.canvas.create_rectangle(130+dx*i, 400-self.height*i, 
                                                250-dx*i, 400-self.height*(i+1), outline='black', 
                                                fill='#{:02x}{:02x}{:02x}'.format(randint(0, 255), 
                                                                                randint(0,255), randint(0, 255)))
            self.stick1_list.append(disk)
        self.sticks_list = [self.stick1_list, self.stick2_list, self.stick3_list]
        self.canvas.update()
        sleep(0.5)

    def move_to(self, stick1, stick2):
        source = self.sticks_list.index(stick1)
        target = self.sticks_list.index(stick2)

        self.canvas.move(stick1[-1], 0, -(210+self.height)+len(stick1)*self.height)
        self.canvas.update()
        sleep(0.2)
        self.canvas.move(stick1[-1], 200*(target-source), 0)
        self.canvas.update()
        sleep(0.2)
        self.canvas.move(stick1[-1], 0, 210+self.height-(len(stick2)+1)*self.height)
        self.canvas.update()
        sleep(0.2)
        stick2.append(stick1.pop())
        self.sticks_list[source] = stick1
        self.sticks_list[target] = stick2

    def solver(self, n, stick1, stick2, stick3):
        if n == 0:
            return
        self.solver(n-1, stick1, stick3, stick2) 
        self.move_to(stick1, stick2)
        self.solver(n-1, stick3, stick2, stick1)

    def launch_solver(self):
        try:
            self.create_disks()
            self.start_button.config(state='disabled')
            if self.n % 2 == 0:
                self.solver(self.n, self.stick1_list, self.stick3_list, self.stick2_list)
            else:
                self.solver(self.n, self.stick1_list, self.stick2_list, self.stick3_list)
            self.start_button.config(state='normal')
        except ValueError:
            mb.showwarning('Увага', 'Поле повинно бути заповнено та містити ціле число!')

    def create_options(self):
        Label(self.frame, font=self.def_font, text='Кількість дисків:').grid(row=0, column=0, sticky='e', pady=10)
        self.disks_entry = Entry(self.frame, font=self.def_font)
        self.disks_entry.grid(row=0, column=1, sticky='w', pady=10, padx=10)
        self.start_button = Button(self.frame, font=self.def_font, text='Почати', width=15, command=self.launch_solver)
        self.start_button.grid(row=0, column=2, pady=10, padx=5, sticky='w')

if __name__ == '__main__':
    program = HanoiGUI()
    mainloop()