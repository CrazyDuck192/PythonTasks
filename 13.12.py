from math import sqrt

class Point2:
    """Клас реалізує точку площини"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        """Повернути координату х"""
        return self._x

    def get_y(self):
        """Повернути координату y"""
        return self._y

    def __str__(self):
        """Повернути рядок представлення точки"""
        return "({}, {})".format(self._x, self._y)

class Rectangle:

    def __init__(self, APoint, width, height):

        self.A = APoint
        self.w = abs(width)
        self.h = abs(height)

        self.B = Point2(self.A.get_x(), self.A.get_y() + self.h)
        self.C = Point2(self.A.get_x() + self.w, self.A.get_y() + self.h)
        self.D = Point2(self.A.get_x() + self.w, self.A.get_y())

        self.points = {'A': self.A, 'B': self.B, 'C': self.C, 'D': self.D}

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def output(self):
        for point, coords in self.points.items():
            print(f"{point}{coords}")

    def intersect(self, rect):
        ax = max(self.A.get_x(), rect.A.get_x())
        ay = max(self.A.get_y(), rect.A.get_y())

        cx = min(self.C.get_x(), rect.C.get_x())
        cy = min(self.C.get_y(), rect.C.get_y())

        if cx > ax and cy > ay:
            A = Point2(ax, ay)
            return Rectangle(A, cx-ax, cy-ay)
        return None


class Point2Ex(Point2):

    def __init__(self, x, y):
        super().__init__(x, y)

    def dist(self):
        return sqrt(self.get_x()**2 + self.get_y()**2)

    def __repr__(self):
        return f"P{self.x},{self.y}"

    def __eq__(self, p):
        return p.get_x() == self.get_x() and p.get_y() == self.get_y()

    def __lt__(self, p):
        return self.dist() < p.dist() 

    def __add__(self, p):

        return Point2Ex(self.get_x() + p.get_x(), self.get_y() + p.get_y())

if __name__ == "__main__":
    rect = Rectangle(Point2(0, 0), 2, 2)
    rect.output()

    spisokRect = []

    n = int(input('n='))
    for _ in range(n):
        x = int(input('x: '))
        y = int(input('y: '))
        p = Point2(x, y)
        w = int(input('Width: '))
        h = int(input('Height: '))
        r = Rectangle(p, w, h)

        spisokRect.append(r)

    inters = spisokRect[0]
    for r in spisokRect[1:]:
        if inters is None: 
            break 
        inters = inters.intersect(r)

    if inters is None:
        print("No intersection")
    else:
        print(f"Area of intersection is {inters.area()}, Perimeter is {inters.perimeter()}")



    x_max = max([r.points['C'].get_x() for r in spisokRect])
    x_min = min([r.points['A'].get_x() for r in spisokRect])
    y_max = max([r.points['C'].get_y() for r in spisokRect])
    y_min = min([r.points['A'].get_y() for r in spisokRect])

    rects_area = [[0 for _ in range(x_min, x_max)] for _ in range(y_min, y_max)]

    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            for rect in spisokRect:
                if rect.A.get_x() < x <= rect.C.get_x() and \
                    rect.A.get_y() < y <= rect.C.get_y():
                    if  y_min <= 0:
                        i = y - 1 + abs(y_min) 
                    else:
                        i = y - 1 - y_min
                    if x_min <= 0:
                        j = x - 1 + abs(x_min)
                    else:
                        j = x - 1 - x_min
                    rects_area[i][j] = 1

    area = 0
    for row in rects_area[::-1]:
        area += row.count(1)
    
    print(f'Area of union is {area}')

