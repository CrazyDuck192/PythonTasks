import turtle as t
from math import *
from time import sleep

class Arrow:

    def __init__(self, x0, y0, x1, y1, color):

        self.x0 = x0
        self.y0 = y0

        self.x1 = x1
        self.y1 = y1

        self.color = color

    def draw(self):
        self.clear()
        t.color(self.color)
        t.setpos(self.x1, self.y1)

    def clear(self):
        t.down()
        t.color(t.bgcolor())
        t.goto(self.x0, self.y0)

class Dial:

    def __init__(self, x0, y0, r, color):

        self.x0 = x0
        self.y0 = y0
        self.r = r
        self.color = color

    def draw(self):
        t.color(self.color)
        t.up()
        t.goto(self.x0, self.y0 - self.r)
        t.down()
        t.circle(self.r)
        t.up()


class Digit:

    def __init__(self, x0, y0, w, h, number, color):

        self.x0 = x0
        self.y0 = y0
        self.w = w
        self.h = h
        self.number = number
        self.color = color

    def draw(self):
        t.color(self.color)

        if self.number == 1:
            t.up()
            t.goto(self.x0, self.y0)
            t.down()
            t.goto(self.x0, self.y0 + self.h)

        elif self.number == 2:
            t.up()
            t.goto(self.x0, self.y0)
            t.down()
            t.goto(self.x0, self.y0 + self.h)
            t.up()
            t.goto(self.x0 + self.w/2, self.y0)
            t.down()
            t.goto(self.x0 + self.w/2, self.y0 + self.h)

        elif self.number == 3:
            t.up()
            t.goto(self.x0, self.y0)
            t.down()
            t.goto(self.x0, self.y0 + self.h)
            t.up()
            t.goto(self.x0 + self.w/2, self.y0)
            t.down()
            t.goto(self.x0 + self.w/2, self.y0 + self.h)
            t.up()
            t.goto(self.x0 + self.w, self.y0)
            t.down()
            t.goto(self.x0 + self.w, self.y0 + self.h)

        elif self.number == 4:
            t.up()
            t.goto(self.x0, self.y0)
            t.down()
            t.goto(self.x0, self.y0 - self.h)
            t.up()
            t.goto(self.x0, self.y0)
            t.down()
            t.goto(self.x0 + self.w/2, self.y0 - self.h)
            t.goto(self.x0 + self.w, self.y0)  

        elif self.number == 5:
            t.up()
            t.goto(self.x0, self.y0)
            t.down()
            t.goto(self.x0 + self.w/2, self.y0 - self.h)
            t.goto(self.x0 + self.w, self.y0)

        elif self.number == 6:
            t.up()
            t.goto(self.x0 - self.w/2, self.y0)
            t.down()
            t.goto(self.x0, self.y0 - self.h)
            t.goto(self.x0 + self.w/2, self.y0)
            t.goto(self.x0 + self.w/2, self.y0 - self.h)

        elif self.number == 7:
            t.up()
            t.goto(self.x0 - self.w * 1.5, self.y0)
            t.down()
            t.goto(self.x0 - self.w, self.y0 - self.h)
            t.goto(self.x0 - self.w * 0.5, self.y0)
            t.goto(self.x0 - self.w * 0.5, self.y0 - self.h)
            t.up()
            t.goto(self.x0, self.y0)
            t.down()
            t.goto(self.x0, self.y0 - self.h)

        elif self.number == 8:
            t.up()
            t.goto(self.x0 - self.w * 2, self.y0)
            t.down()
            t.goto(self.x0 - self.w * 1.5, self.y0 - self.h)
            t.goto(self.x0 - self.w, self.y0)
            t.goto(self.x0 - self.w, self.y0 - self.h)
            t.up()
            t.goto(self.x0 - self.w * 0.5, self.y0)
            t.down()
            t.goto(self.x0 - self.w * 0.5, self.y0 - self.h)
            t.up()
            t.goto(self.x0, self.y0)
            t.down()
            t.goto(self.x0, self.y0 - self.h)

        elif self.number == 9:
            t.up()
            t.goto(self.x0 - self.w - 3, self.y0)
            t.down()
            t.goto(self.x0 - self.w - 3, self.y0 + self.h)
            t.up()
            t.goto(self.x0 - self.w, self.y0)
            t.down()
            t.goto(self.x0, self.y0 + self.h)
            t.up()
            t.goto(self.x0 - self.w, self.y0 + self.h)
            t.down()
            t.goto(self.x0, self.y0)

        elif self.number == 10:
            t.up()
            t.goto(self.x0, self.y0 + self.h)
            t.down()
            t.goto(self.x0 - self.w, self.y0)
            t.up()
            t.goto(self.x0 - self.w, self.y0 + self.h)
            t.down()
            t.goto(self.x0, self.y0)

        elif self.number == 11:
            t.up()
            t.goto(self.x0, self.y0)
            t.down()
            t.goto(self.x0, self.y0 + self.h)
            t.up()
            t.goto(self.x0 - 3, self.y0 + self.h)
            t.down()
            t.goto(self.x0 - self.w - 3, self.y0)
            t.up()
            t.goto(self.x0 - self.w - 3, self.y0 + self.h)
            t.down()
            t.goto(self.x0 - 3, self.y0)

        elif self.number == 12:
            t.up()
            t.goto(self.x0, self.y0)
            t.down()
            t.goto(self.x0 - self.w, self.y0 + self.h)
            t.up()
            t.goto(self.x0 - self.w, self.y0)
            t.down()
            t.goto(self.x0, self.y0 + self.h)
            t.up()
            t.goto(self.x0 + 3, self.y0 + self.h)
            t.down()
            t.goto(self.x0 + 3, self.y0)
            t.up()
            t.goto(self.x0 + 3 + self.w/2, self.y0 + self.h)
            t.down()
            t.goto(self.x0 + 3 + self.w/2, self.y0) 
            


if __name__ == '__main__':

    def prep_clock(radius = 200, num_w = 30, num_h = 40):
        t.hideturtle()
        t.speed(100)
        d = Dial(0, 0, radius, 'red')
        d.draw()

        digits = [i for i in range(1, 13)]
        for num in digits:
            x0 = radius*sin(2*pi/360*30*num)
            y0 = radius*cos(2*pi/360*30*num)
            if num == 3:
                x0 += 2
            dig = Digit(x0, y0, num_w, num_h, num, 'black')
            dig.draw()

        t.up()
        ar_s = Arrow(0, 0, (radius-3)*sin(2*pi/360*30*0), (radius-3)*cos(2*pi/360*30*0), 'green')
        ar_s.draw()

        t.speed(3)

    def timer(seconds = 0, minutes = 0, radius = 200):
        for _ in range(1, 61):
            sleep(1)
            seconds += 1
            if seconds % 5 == 0:
                print(f'Пройшло: \nхвилин: {minutes}, секунд: {seconds}')
                ar_s = Arrow(0, 0, (radius-3)*sin(2*pi/360*30/5*seconds), (radius-3)*cos(2*pi/360*30/5*seconds), 'green')
                ar_s.draw()
        minutes += 1
        timer(0, minutes)

    
    prep_clock()
    timer()
    
    t.exitonclick()
        



