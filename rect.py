import turtle
class Point:
    '''Точка екрану
    '''
    _count = 0
    def __init__(self, x, y):
        self._x = x # _x - координата x точки
        self._y = y # _y - координата y точки
        self._visible = False # _visible - чи є точка
        # видимою на екрані
        Point._count += 1
    def getx(self):
        '''Повертає координату x точки
        '''
        return self._x
    def gety(self):
        '''Повертає координату y точки
        '''
        return self._y
    def onscreen(self):
        '''Перевіряє, чи є точка видимою на екрані
        '''
        return self._visible
    def switchon(self):
        
        '''Робить точку видимою на екрані
        '''
        if not self._visible:
            self._visible = True
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.down()
            turtle.dot()
    def switchoff(self):
        '''Робить точку невидимою на екрані
        '''
        if self._visible:
            self._visible = False
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.down()
            turtle.dot(turtle.bgcolor())
        
    def move(self, dx, dy):
        '''Пересуває точку на екрані на dx, dy позицій
        '''
        vis = self._visible
        if vis:
            self.switchoff()
        self._x += dx
        self._y += dy
        if vis:
            self.switchon()

    def printcount():
        return Point._count
    
    printcount = staticmethod(printcount)

class Rectangle:

    def __init__(self, A, width, height):
        self.A = A
        self.width = width
        self.height = height
        self.B = Point(self.A.getx() + self.width, self.A.gety())
        self.C = Point(self.A.getx() + self.width, self.A.gety() - self.height)
        self.D = Point(self.A.getx(), self.A.gety() - self.height)

    def getAB(self):
        return self.width

    def getBC(self):
        return self.height

    def getCD(self):
        return self.width

    def getAD(self):
        return self.height

    def draw(self):
        self.A.switchon()
        turtle.setpos(self.B.getx(), self.B.gety())
        self.B.switchon()
        turtle.setpos(self.C.getx(), self.C.gety())
        self.C.switchon()
        turtle.setpos(self.D.getx(), self.D.gety())
        self.D.switchon()
        turtle.setpos(self.A.getx(), self.A.gety())

    def clear(self):
        turtle.color(turtle.bgcolor())
        self.A.switchoff()
        turtle.setpos(self.B.getx(), self.B.gety())
        self.B.switchoff()
        turtle.setpos(self.C.getx(), self.C.gety())
        self.C.switchoff()
        turtle.setpos(self.D.getx(), self.D.gety())
        self.D.switchoff()
        turtle.setpos(self.A.getx(), self.A.gety())

    def move(self, dx, dy):
        self.clear()
        turtle.color('black')
        self.A.move(dx, dy)
        self.B.move(dx, dy)
        self.C.move(dx, dy)
        self.D.move(dx, dy)
        self.draw()


    
        

if __name__ == "__main__":    
    n = int(input('n = '))
    rects = []
    for _ in range(n):
        x = int(input('x = '))
        y = int(input('y = '))
        p = Point(x, y)
        w = int(input('width = '))
        h = int(input('height = '))
        rect = Rectangle(p, w, h)
        dx = int(input('dx = '))
        dy = int(input('dy = '))
        rects.append((rect, dx, dy))

    for rect in rects:
        rect[0].draw()
        rect[0].move(rect[1], rect[2])
    turtle.exitonclick()

    


