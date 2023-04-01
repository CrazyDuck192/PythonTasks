"""Описати абстрактний клас Shape (геометрична фігура) та
його нащадки Circle (коло), Rectangle (прямокутник), Triangle
(трикутник). Передбачити у Shape властивості обчислення
периметру та площі фігури а також метод, що перевіряє, чи
перетинаються дві фігури.
З використанням цих класів розв’язати задачу. Дано список
геометричних фігур, що не перетинаються. Перевірити, чи
справді вони не перетинаються та порахувати їх сумарну площу."""

from abc import ABCMeta, abstractmethod
import math

class Shape(metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def intersect(self, other):
        pass
    
class Circle(Shape):

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r
    
    def area(self):
        return math.pi * self.r**2
    
    def intersect(self, other):
        if isinstance(other, Circle):
            return (other.x - self.x)**2 + (other.y - self.y)**2 < (self.r+other.r)**2
        
        return False
    
class Rectangle(Shape):

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def perimeter(self):
        return 2*(self.w + self.h)
    
    def area(self):
        return self.h * self.w

    def intersect(self, other):
        if isinstance(other, Rectangle):
            x1 = min(other.x, self.x)
            x2 = max(other.x + other.w, self.x + self.w)

            y1 = max(other.y, self.y)
            y2 = min(other.y + other.h, self.y + self.h)

            if x1<=x2 and y1<=y2:
                return True
            else:
                return False
            
        elif isinstance(other, Circle):
            return False
        
        return False
    

if __name__ == '__main__':

    n = int(input('n = '))

    figures = []
    for _ in range(n):
        choice = input('Input rect(r) or circle(c) or quit(q)')

        CHOICES = ('r', 'c', 'q')
        while choice not in CHOICES:
            choice = input('Input rect(r) or circle(c) or quit(q)')

        if choice == 'c':
            x, y, r = map(float, input().split())
            c = Circle(x, y, r)
            figures.append(c)

        elif choice == 'r':
            x, y, w, h = map(float, input().split())
            r = Rectangle(x, y, w, h)
            figures.append(r)

        else: break

    sum_area = 0
    for item in figures:
        sum_area += item.area()

    sum_area_1 = sum([f.area() for f in figures])

    print(f'sum area {sum_area}, {sum_area_1}')
