"""Описати декоратор класу, який модифікує клас для
перевірки, чи належать параметри, що використовуються при
ініціалізації об’єкта цього класу, заданим типам. Вважати, що
клас має поле _field_types – словник, що містить імена полів в
якості ключів та типи полів в якості значень. Якщо типи
невідповідні, то ініціює виключення ValueError.
Застосувати цей декоратор до класів Point та Circle (див. тему
«Класи та об’єкти»), та виконати зображення та переміщення
точок та кіл.
"""

class CheckType:

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, **kwargs):
        for k, v in kwargs.items():
            for var, t in self.cls._field_types.items():
                if k == var and type(v) != t:
                    raise ValueError
        return self.cls.__call__(**kwargs)

@CheckType
class Point:
    _field_types = {'x': int, 'y': int}

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Point({self.x}, {self.y})'
    
    def move(self, dx, dy):
        self.center.move(dx, dy)

@CheckType
class Circle:
    _field_types = {'center': Point, 'radius': int}

    def __init__(self, center, radius) -> None:
        self.center = center
        self.radius = radius

    def __str__(self) -> str:
        return f'Circle({self.center}, {self.radius})'
    
    def move(self, dx, dy):
        self.center.move(dx, dy)


if __name__ == '__main__':
    p = Point(x=1, y=2)
    print(p)
    c = Circle(center=Point(x='a',y=2), radius=3)
    print(c)