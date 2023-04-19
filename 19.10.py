"""Описати функцію, яка створює клас-нащадок tuple, що
реалізує розмічене об’єднання.
Розмічене об’єднання – це тип даних, елементи якого можуть
мати різний набір полів в залежності від значення полядискримінанта. Наприклад, точка площини може бути
представлена у декартовій або полярній системі координат.
Отже, поле дискримінанта може називатись syst_coord зі
значеннями ‘cart’, ‘polar’, а відповідні поля у декартовій системі
координат – ‘x’, ‘y’, а у полярній, - ‘ro’, ‘phi’. Доступ до полів
розміченого об’єднання здійснюється наступним чином: a.x або
a.syst_coord.
Параметрами функції, що реалізує розмічене об’єднання,
будуть: ім’я класу, ім’я поля дискримінанта та словник з
ключами, що є значеннями поля дискримінанта, та значеннями –
наборами імен відповідних полів.
Побудований клас повинен забороняти доступ до полів, які
відсутні (при заданому значенні поля дискримінанта).
Використавши цю функцію, побудувати клас для точки
площини, що може бути задана у декартовій або полярній системі
координат.
Нехай дано 3 точки площини у декартовій або полярній
системі координат. Обчислити площу трикутника, утвореного
цими точками."""
from math import sqrt, cos, sin, pi

def union(name, syst_name, dct):
    cls_dict = {}
    def getter(n, name=""):
        def _getter(self):
            if name and name not in dct[getattr(self, syst_name)]:
                raise AttributeError("Розмічене об`єднання з дискримінантом '{}' "
                                     "не має атрибута '{}'"
                                     .format(getattr(self, syst_name), name))
            return self[n]
        return _getter
    
    cls_dict[syst_name] = property(getter(0))
    for names in dct.values():
        for i, param in enumerate(names, 1):
            cls_dict[param] = property(getter(i, param))

    def __new__(cls, *args):
        assert len(args) == len(dct[args[0]])+1, 'Lengths not equal'
        return tuple.__new__(cls, args)
    
    cls_dict['__new__'] = __new__
    cls = type(name, (tuple,), cls_dict)
    return cls

def to_cart(p):
    assert p.syst in ('cart', 'polar'), 'Incorrect syst'
    if p.syst == 'polar':
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
    Point = union('Point', 'syst', {'cart': ('x', 'y'), 'polar': ('ro', 'phi')})
    p_1 = Point('cart', 1, 3)
    p_2 = Point('polar', 2, 60)
    p_3 = Point('cart', 2, 3)
    print(p_1.ro)
    print(p_1, p_2, p_3)
    s = area(p_1, p_2, p_3)
    print(s)

        