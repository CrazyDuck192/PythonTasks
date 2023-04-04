class Point:

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def input(self):
        self.x = float(input('x = '))
        self.y = float(input('y = '))

class CompareMixin:

    def __eq__(self, other):
        return not (self.__lt__(other) or other.__lt__(self))
    
    def __gt__(self, other):
        return other.__lt__(self)
    
    def __ne__(self, other):
        return self.__lt__(other) or other.__lt__(self)
    
    def __ge__(self, other):
        return not self.__lt__(other)
    
    def __le__(self, other):
        return not other.__lt__(self)
    
class Point2(Point, CompareMixin):
    pass

class XOrderPoint2(Point2):

    def __lt__(self, other):
        return self.x<other.x
    
class YOrderPoint2(Point2):

    def __lt__(self, other):
        return self.y < other.y

class DistOrderPoint2(Point2):

    def __lt__(self, other):
        return (self.x**2+self.y**2)**0.5 < (other.x**2+other.y**2)**0.5

if __name__ == '__main__':
    n = int(input('n = '))
    points_list = []
    for _ in range(n):
        a = DistOrderPoint2()
        a.input()
        points_list.append(a)
    points_list = sorted(points_list)[::-1]
    for i in points_list:
        print(i)

    

    