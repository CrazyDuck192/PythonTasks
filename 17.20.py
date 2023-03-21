def check_type(*typechecker):

    def _check_type(func):

        def __check_type(*args, **kwargs):

            try:
                if len(typechecker) != len(args):
                    raise TypeError('Amounts do not match')
            except TypeError:
                return TypeError('Amounts do not match')
            
            try:
                for i, t in zip(args, typechecker):
                    if type(i) != t:
                        raise TypeError('Types do not match')
            except TypeError:
                return TypeError('Types do not match')
            
            y = func(*args, **kwargs)
            return y
        
        return __check_type
    
    return _check_type

class TypeError(Exception):

    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return self.msg

@ check_type(int, str, tuple)   
def func(a, b, c):
    return f'| {a} | {b} | {c} |'


if __name__ == '__main__':
    print(func(22, 'hello', (1, 'hi', 2)))
    print(func(22.5, 'hello', (1, 'hi', 2)))
    print(func(22,'hello world'))

    
                
            