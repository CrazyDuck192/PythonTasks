"""Описати декоратор класу, який здійснює модифікацію
класу з метою трасування виклику усіх власних (не спеціальних)
методів класу. Під час трасування показувати ім’я методу,
значення параметрів до виклику, а також результат після
виклику. Застосувати цей декоратор до класів Person та Student
(див. тему «Класи та об’єкти») та виконати програму обчислення
стипендії студентам"""

def trace(func):

    def _trace(*args, **kwargs):

        print(f'Name of function: {func.__name__}')
        for x in args:
            print(x)
        for k, v in kwargs.items():
            print(f'{k} = {v}')
        y = func(*args, **kwargs)
        print(y)
        return y

    return _trace

def class_tracing(cls):
    for name, attr in cls.__dict__.items():
        if not name.startswith('__') and callable(attr):
            setattr(cls, name, trace(attr))

    return cls

@class_tracing
class Functions:

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
        
    def factorial(self, n):
        if n <= 1:
            return 1
        else:
            return n*self.factorial(n-1)
        
    def const(self, const):
        return const
    

if __name__ == '__main__':
    a = Functions(1,2,3)
    a.factorial(5)
    a.const(77)