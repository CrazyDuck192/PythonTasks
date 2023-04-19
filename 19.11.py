from math import cos, sin, sqrt, pi
import operator

class UnionTupleMeta(type):
    
    def __init__(cls, name, bases, nmspc):
        super().__init__(name, bases, nmspc)
        value = nmspc['discriminant']
        setattr(cls, value, property(operator.itemgetter(0)))
        if cls.params:
            for params in list(cls.params.values()):
                for i, name, in enumerate(params, 1):
                    setattr(cls, name, property(operator.itemgetter(i)))

class UnionTuple(tuple, metaclass=UnionTupleMeta):
    discriminant = ''
    params = {}

    def __new__(cls, *args):
        if len(args) != len(cls.params[list(cls.params.keys())[0]])+1:
            raise ValueError
        return tuple.__new__(cls, args)
    
def to_cart(p):
    if p.system == 'polar':
        x = p.ro * cos(p.phi * pi/180)
        y = p.ro * sin(p.phi * pi/180)
        return (x, y)
    return (p.x, p.y)

def dist(p_1, p_2):
    a = to_cart(p_1)
    b = to_cart(p_2)
    return sqrt((a[0] - b[0])**2 + (a[1]- b[1])**2)

def area(p_1, p_2, p_3):
    a = dist(p_1, p_2)
    b = dist(p_2, p_3)
    c = dist(p_1, p_3)
    p = (a+b+c)/2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    return s
        

if __name__ == '__main__':
    class Point(UnionTuple):
        discriminant = 'system'
        params = {'cart': ('x', 'y'), 'polar': ('ro', 'phi')}

    p_1 = Point('cart', 1, 3)
    p_2 = Point('polar', 2, 60)
    p_3 = Point('cart', 3, 3)
    print(p_1, p_2, p_3)
    s = area(p_1, p_2, p_3)
    print(s)
    
        