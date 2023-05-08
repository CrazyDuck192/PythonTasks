class ObjCounter:

    count = 0
    obj_type = None

    def __init__(self) -> None:
        ObjCounter.obj_type = self.__class__.__name__
        ObjCounter.count += 1

    @staticmethod
    def printcount():
        print(f"Кількість: {ObjCounter.count}\nТип: {ObjCounter.obj_type}")


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


class Point2ObjCounter(ObjCounter, Point2):
    
    def __init__(self, x, y) -> None:
        ObjCounter.__init__(self)
        Point2.__init__(self, x, y)

if __name__ == '__main__':
    coords = '3, 4, 6, 8, 1, 2, 5, 5, 3, 3'
    points = list(map(int, coords.split(', ')))
    i = 0
    if len(points) % 2 == 0:
        while i != len(points):
            p = Point2ObjCounter(points[i], points[i+1])
            print(p)
            i += 2
    else:
        raise Exception

    Point2ObjCounter.printcount()