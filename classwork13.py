# Завдання 17.1
def make_positive(fun):

    def _make_positive(*args, **kwargs):

        y = fun(*args, **kwargs)
        if y < 0:
            return 0
        return y
    
    return _make_positive

@ make_positive
def f1(x):
    return 2*x-1


@ make_positive
def f2(x, y):
    return 2*x-y

# Завдання 17.2
def make_x(a, b):

    def _make_x(fun):

        def __make_x(*args, **kwargs):

            y = fun(*args, **kwargs)
            if y >= a and y <= b:
                return y
            else:
                return (a+b)/2
            
        return __make_x
    
    return _make_x

@make_x(1, 5)
def f3(x):
    return x**2

def check_args(func):

    def _check_args(*args, **kwargs):
        try:
            y = func(*args, **kwargs)
            if len(args) == len(kwargs):
                return y
            else:
                raise LengthError
        except LengthError:
            return LengthError()
        
    return _check_args

class LengthError(Exception):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Length error'

@check_args
def func_2(*x, **y):
    s = 1
    for a, b in enumerate(y.keys()):
        s *= (x[a] + 1/y[b])
    return s

# Завдання 17.4
def check_str(func):

    def _check_str(*args):
        try:
            for x in args:
                if type(x) != str:
                    raise TypeError
        except TypeError:
            return TypeError('All args must be a string')
            
        return func(*args)
            
    return _check_str

@ check_str
def string(*args):
    return list(set(x for x in args))

# Завдання 17.5
def check_type(t):

    def _check_type(func):

        def __check_type(*args, **kwargs):

            try:
                for i in args:
                    if type(i) != t:
                        raise TError
            except TError:
                return TError()

            return func(*args, **kwargs)
        
        return __check_type
    
    return _check_type

class TError(Exception):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Wrong type'


@check_type(int)
def func(x, y):
    return x**2 + y**2


# Завдання 17.6
def check_args(func):

    def _check_args(*args, **kwargs):
        try:
            if len(kwargs) > 0:
                raise ValueError
        except ValueError:
            return ValueError('It must be only args, not kwargs')
        
        return func(*args)
    
    return _check_args

@ check_args
def func_1(*args):
    return 1 if max(args) > sum(args) else sum([arg for arg in args if arg > 0])

if __name__ == '__main__':
    # 17.1
    print(f1(1), f1(0))
    print(f2(1,1), f2(0, 1))

    # 17.2
    print(f3(2), f3(3)) 

    # 17.3
    f = func_2(2, 3, 4, y1 = 2, y2 = 3)
    print(f)
    f = func_2(3, 2, 3, y1=2, y2=3, y3=4)
    print(f)   

    # 17.4
    print(string('abc', 'bbb', 'aa', 'a', 'bbb', 'ab', 'abc'))
    print(string('abc', '0', 1, 2, 3))

    # 17.5
    print(func(2, 3))
    print(func(2.5, 3))

    # 17.6
    print(func_1(2, 3, 4, -2, -5))
    print(func_1(3, 4, 5, y=5))

