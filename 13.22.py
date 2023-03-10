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

    def __lt__(self, other):
        if sqrt(self._x**2 + self._y**2) < sqrt(other._x**2 + other._y**2):
            return True
        return False
    
    def __gt__(self, other):
        if sqrt(self._x**2 + self._y**2) > sqrt(other._x**2 + other._y**2):
            return True
        return False
    
    def __eq__(self, other):
        if sqrt(self._x**2 + self._y**2) == sqrt(other._x**2 + other._y**2):
            return True
        return False
    
    def __ne__(self, other):
        if sqrt(self._x**2 + self._y**2) != sqrt(other._x**2 + other._y**2):
            return True
        return False
    

if __name__ == '__main__':
    points = []
    n = int(input('n = '))

    for _ in range(n):
        x = int(input('x = '))
        y = int(input('y = '))
        p = Point2Ex(x, y)
        points.append(p)

    y = [p for p in sorted(points)][0]
    print(y)
    length = 0

    for x in [p for p in sorted(points)[1:]]:
        print(x)
        length += sqrt((y.get_x() - x.get_x())**2 + (y.get_y() - x.get_y())**2)
        y = x

    print(f'Довжина ламаної: {length}')


