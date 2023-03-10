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
    
class Point2Ex(Point2):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __eq__(self, other):
        if self.get_x() == other.get_x() and self.get_y() == other.get_y():
            return True
        return False
    
    def __ne__(self, other):
        if self.get_x() != other.get_x() or self.get_y() != other.get_y():
            return True
        return False
    
class Segment:
    """Клас реалізує відрізок на площині"""
    def __init__(self, a, b):
        self._a = a # точка
        self._b = b # точка

    def get_a(self):
        """Повернути точку a"""
        return self._a
    
    def get_b(self):
        """Повернути точку b"""
        return self._b
    
    def __str__(self):
        """Повернути рядок представлення відрізку"""
        return "[{}, {}]".format(self._a, self._b)
    
    def len(self):
        return sqrt((self._a.get_x() - self._b.get_x())
        ** 2 +
        (self._a.get_y() - self._b.get_y())
        ** 2)
    
class SegmentEx(Segment):

    def __init__(self, a, b):
        super().__init__(a, b)

    def __lt__(self, other):
        if self.len() < other.len():
            return True
        return False
    
    def __gt__(self, other):
        if self.len() > other.len():
            return True
        return False
    
    def __eq__(self, other):
        if self.len() == other.len():
            return True
        return False
    
    def __ne__(self, other):
        if self.len() != other.len():
            return True
        return False
    
    def on_line(self, other):
        segments_list = [SegmentEx(self.get_a(), other.get_a()),
                         SegmentEx(self.get_a(), other.get_b()),
                         SegmentEx(self.get_b(), other.get_a()),
                         SegmentEx(self.get_b(), other.get_b())]
        for s in segments_list:
            if (s.get_b().get_x() - s.get_a().get_x())/(self.get_b().get_x() - self.get_a().get_x()) !=\
                (s.get_b().get_y() - s.get_a().get_y())/(self.get_b().get_y() - self.get_a().get_y()):
                return False
            
        return True
    
if __name__ == '__main__':

    # A = Point2Ex(0, 0)
    # B = Point2Ex(3, 3)
    # C = Point2Ex(2, 2)
    # D = Point2Ex(5, 5)
    # AB = SegmentEx(A, B)
    # CD = SegmentEx(C, D)
    # print(AB.on_line(CD))

    n = int(input('n = '))
    segments_list = []
    points = []

    for _ in range(n):
        x_1 = int(input('x_1 = '))
        y_1 = int(input('y_1 = '))
        a = Point2Ex(x_1, y_1)
        x_2 = int(input('x_2 = '))
        y_2 = int(input('y_2 = '))
        b = Point2Ex(x_2, y_2)
        ab = SegmentEx(a, b)
        points.append(a)
        points.append(b)
        segments_list.append(ab)

    is_poly = True  
    is_regular = False
    for p in points:
        if points.count(p) != 2:
           is_poly = False

    length = segments_list[0].len()
    if all([x.len() == length for x in segments_list]):
        is_regular = True

    if is_poly:
        print('Відрізки складають многокутник \2')
    else:
        print('Відрізки не складають многокутник')

    if is_regular:
        print('Многокутник є правильним \2')
    else:
        print('Многокутник не є правильним')


    
    

